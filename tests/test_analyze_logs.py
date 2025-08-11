import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from analyzer import analyze_logs


def test_analyze_logs_handles_string_levels(tmp_path):
    log_entries = [
        {"time": "2023-01-01T00:00:00Z", "level": "ERROR", "msg": "fail"},
        {"time": "2023-01-01T00:01:00Z", "level": "warning", "msg": "warn"},
        {"time": "2023-01-01T00:02:00Z", "level": "info", "msg": "note"},
    ]
    log_file = tmp_path / "log.json"
    with log_file.open('w', encoding='utf-8') as f:
        for entry in log_entries:
            f.write(json.dumps(entry) + "\n")

    results = analyze_logs(log_file, min_level=30)

    assert results['total_error_count'] == 2
    labels = results['chart_data_severity']['labels']
    data = results['chart_data_severity']['data']
    severity = dict(zip(labels, data))
    assert severity.get('ERROR') == 1
    assert severity.get('WARNING') == 1
