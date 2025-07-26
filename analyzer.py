# analyzer.py
import json
import logging
from collections import defaultdict

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
        # This case should be handled by the calling function, but it's a safeguard.
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
    """Parses logs, groups entries by level, and returns a summary."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        log_queue = data.get('queue', data.get('logs', []))
        error_entries = []

        for item in log_queue:
            try:
                log_entry = json.loads(item) if isinstance(item, str) else item
                if isinstance(log_entry, dict) and log_entry.get('level', 0) >= min_level:
                    error_entries.append(log_entry)
            except (json.JSONDecodeError, TypeError):
                continue
        
        if not error_entries:
            logging.info(f"No log entries found with level >= {min_level}.")

        summary = defaultdict(lambda: {'Message': '', 'Count': 0, 'LastSeen': ''})
        for entry in error_entries:
            msg = entry.get('msg', 'Unknown Error')
            summary[msg]['Message'] = msg
            summary[msg]['Count'] += 1
            summary[msg]['LastSeen'] = entry.get('time', '')

        return {
            'summary': sorted(summary.values(), key=lambda x: x['Count'], reverse=True),
            'all_errors': error_entries
        }
    except Exception as e:
        logging.error(f"Error analyzing logs at '{file_path}': {e}")
        return {'summary': [], 'all_errors': []}

def analyze_settings(file_path):
    """Parses the main settings file, handling both list and dict formats."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # This logic handles both list-based and dictionary-based settings files.
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
        
        # This logic robustly handles list, nested dict, and flat dict formats.
        if isinstance(data, list):
            settings_list = data
        elif isinstance(data, dict):
            settings_list = data.get('config', {}).get('settings', []) or data.get('settings', []) or data
            if isinstance(settings_list, dict):
                 settings_list = [{'_id': k, 'value': v} for k, v in settings_list.items()]
        else:
            settings_list = []
        
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
