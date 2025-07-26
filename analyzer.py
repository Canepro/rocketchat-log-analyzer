# analyzer.py
import json
import logging
from collections import defaultdict

# Knowledge base for providing recommendations based on log messages
RECOMMENDATIONS = {
    "API rate limit exceeded": "High API usage detected. Consider increasing the API rate limiter settings under Admin > General > API.",
    "MongoTimeoutException": "Database connection timed out. Verify the MongoDB server is running, accessible, and not under heavy load.",
    "Cannot read property 'rid' of null": "This is a common but often benign error related to real-time updates. If it spams the logs, it may indicate an issue with a specific integration or app.",
    "E11000 duplicate key error": "A database write operation failed due to a duplicate key. This can happen during data migrations or if an app is misbehaving. The system usually recovers, but frequent occurrences should be investigated.",
    "LDAP Login failed": "LDAP authentication failed. Check the LDAP server connection, bind credentials, and user search filters in Admin > LDAP.",
    "No agents available": "No agents available in Omnichannel. Verify agents are online and departments are configured correctly."
}

def _format_value(value):
    """Formats a setting's value into a string, handling dicts/lists."""
    if isinstance(value, (dict, list)):
        return json.dumps(value, indent=2, ensure_ascii=False)
    if value is None:
        return ''
    return str(value)

def _process_settings_list(settings_list, key_field='_id', value_field='value'):
    """Helper to process a list of setting objects, redacting sensitive keys."""
    analyzed = []
    sensitive_substrings = {'password', 'secret', 'token'}

    if not isinstance(settings_list, list):
        logging.warning(f"Input for settings processing was not a list, it was {type(settings_list)}.")
        return []

    for item in settings_list:
        if not isinstance(item, dict) or key_field not in item:
            continue

        key = item.get(key_field, '')
        key_lower = key.lower()
        value = item.get(value_field)

        if any(s_key in key_lower for s_key in sensitive_substrings):
            value_str = 'REDACTED'
        else:
            value_str = _format_value(value)

        analyzed.append({'Setting': key, 'Value': value_str})
    return analyzed

def analyze_logs(file_path, min_level=50):
    """Parses logs from a Rocket.Chat support dump file."""
    found_entries = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Try to load the whole file as a single JSON object (standard dump format)
        try:
            data = json.loads(content)
            if 'queue' in data and isinstance(data['queue'], list):
                for item in data['queue']:
                    if isinstance(item, dict) and 'string' in item:
                        try:
                            # The actual log is an escaped JSON string within the 'string' field
                            log_entry = json.loads(item['string'])
                            found_entries.append(log_entry)
                        except (json.JSONDecodeError, TypeError):
                            continue # Ignore malformed strings
        except json.JSONDecodeError:
            # If the above fails, fall back to line-by-line parsing for other formats (e.g., JSONL)
            logging.info("Could not parse as single JSON object with a queue, falling back to line-by-line parsing.")
            for line in content.splitlines():
                try:
                    if line.strip():
                        found_entries.append(json.loads(line))
                except json.JSONDecodeError:
                    if line.strip() and not line.strip().startswith('{'):
                         found_entries.append({'msg': line.strip(), 'level': None})
                    else:
                        logging.warning(f"Skipping malformed line: {line.strip()}")

        # Filter entries by the minimum log level
        filtered_entries = [
            entry for entry in found_entries
            if (entry.get('level') is not None and entry.get('level') >= min_level) or \
               (entry.get('level') is None and min_level <= 20) # Include level-less entries for INFO/DEBUG
        ]
        
        total_entry_count = len(filtered_entries)
        if not filtered_entries:
            logging.info(f"No log entries found with level >= {min_level}.")

        limited_entries = filtered_entries[-500:]

        summary = defaultdict(lambda: {'Message': '', 'Count': 0, 'LastSeen': ''})
        recommendations = set()

        for entry in filtered_entries:
            msg = entry.get('msg', 'Unknown Error')
            summary[msg]['Message'] = msg
            summary[msg]['Count'] += 1
            summary[msg]['LastSeen'] = entry.get('time', '')
            
            for keyword, recommendation in RECOMMENDATIONS.items():
                if keyword.lower() in msg.lower():
                    recommendations.add(recommendation)

        return {
            'summary': sorted(summary.values(), key=lambda x: x['Count'], reverse=True),
            'all_errors': limited_entries,
            'total_error_count': total_entry_count,
            'recommendations': list(recommendations)
        }
    except Exception as e:
        logging.error(f"Error analyzing logs at '{file_path}': {e}")
        return {'summary': [], 'all_errors': [], 'total_error_count': 0, 'recommendations': []}

def analyze_settings(file_path):
    """Parses the main settings file, handling both list and dict formats."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if isinstance(data, dict):
            settings_list = [{'_id': k, 'value': v} for k, v in data.items()]
        elif isinstance(data, list):
            settings_list = data
        else:
            settings_list = []

        return _process_settings_list(settings_list)
    except Exception as e:
        logging.error(f"Error analyzing settings at '{file_path}': {e}")
        return []

def analyze_apps(file_path):
    """Parses the installed apps file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        apps_list = data.get('apps', []) if isinstance(data, dict) else data
        if not apps_list:
            logging.info("No apps found in apps file.")
        return [{'Name': a.get('name'), 'Version': a.get('version'), 'Status': a.get('status')} for a in apps_list]
    except Exception as e:
        logging.error(f"Error analyzing apps at '{file_path}': {e}")
        return []

def analyze_omnichannel(file_path):
    """Parses omnichannel settings safely from multiple possible structures."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        settings_list = []
        if isinstance(data, dict):
            settings_list = (
                data.get('config', {}).get('settings', []) or data.get('settings', []) or data
            )
            if isinstance(settings_list, dict):
                 settings_list = [{'_id': k, 'value': v} for k, v in settings_list.items()]
        elif isinstance(data, list):
            settings_list = data
        
        if not settings_list:
            logging.warning("Could not find a valid list of settings in omnichannel file.")
            return []
            
        return _process_settings_list(settings_list)
    except Exception as e:
        logging.error(f"Error analyzing omnichannel at '{file_path}': {e}")
        return []

def analyze_statistics(file_path):
    """Parses server statistics and filters out null values."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        stats = {
            'Version': data.get('version'),
            'Total Users': data.get('totalUsers'),
            'Active Users': data.get('activeUsers'),
            'Total Rooms': data.get('totalRooms'),
            'Omnichannel Enabled': data.get('livechatEnabled'),
            'OS Type': data.get('os', {}).get('type'),
            'Node Version': data.get('process', {}).get('nodeVersion'),
            'MongoDB Version': data.get('mongoVersion')
        }
        return [{'Statistic': key, 'Value': str(value)} for key, value in stats.items() if value is not None]
    except Exception as e:
        logging.error(f"Error analyzing statistics at '{file_path}': {e}")
        return []