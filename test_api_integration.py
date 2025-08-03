"""
Integration test for the complete API workflow with real file upload.
"""

import os
import tempfile
import zipfile
import json
import time

def create_realistic_support_dump():
    """Create a realistic support dump ZIP file for testing."""
    temp_dir = tempfile.mkdtemp()
    zip_path = os.path.join(temp_dir, 'realistic_support_dump.zip')
    
    with zipfile.ZipFile(zip_path, 'w') as zf:
        # Create realistic log content
        rocket_log = """
2025-08-03T08:00:00.123Z info: Starting Rocket.Chat server...
2025-08-03T08:00:01.456Z info: MongoDB connection established
2025-08-03T08:00:02.789Z info: Server listening on port 3000
2025-08-03T08:01:15.234Z warn: High memory usage detected: 85%
2025-08-03T08:02:30.567Z error: Failed to connect to external service
2025-08-03T08:02:31.890Z info: Retrying connection...
2025-08-03T08:03:45.123Z error: Database query timeout
2025-08-03T08:04:00.456Z info: User authentication successful
2025-08-03T08:05:12.789Z warn: Rate limiting activated for IP 192.168.1.100
2025-08-03T08:06:25.012Z info: Message sent successfully
2025-08-03T08:07:38.345Z error: WebSocket connection lost
2025-08-03T08:08:51.678Z info: Reconnection established
2025-08-03T08:09:04.901Z debug: Cache cleared
2025-08-03T08:10:17.234Z info: Backup process started
"""
        
        # Add log files
        zf.writestr('logs/rocketchat.log', rocket_log)
        zf.writestr('logs/mongodb.log', '2025-08-03T08:00:00.000Z info: MongoDB started\n')
        zf.writestr('logs/nginx.log', '192.168.1.1 - - [03/Aug/2025:08:00:00 +0000] "GET / HTTP/1.1" 200\n')
        
        # Add support dump metadata
        support_info = {
            "version": "6.5.0",
            "timestamp": "2025-08-03T08:00:00.000Z",
            "server": {
                "os": "Linux",
                "node_version": "18.17.0",
                "rocket_chat_version": "6.5.0"
            }
        }
        zf.writestr('support-dump-info.json', json.dumps(support_info, indent=2))
        
        # Add some system info
        zf.writestr('system/cpu_info.txt', 'CPU: Intel Core i7-9700K\nCores: 8\n')
        zf.writestr('system/memory_info.txt', 'Total: 16GB\nUsed: 8GB\n')
    
    return zip_path

def test_complete_workflow():
    """Test the complete API workflow."""
    from app import create_app
    
    # Create test app
    app = create_app('development')
    
    with app.test_client() as client:
        print("🔍 Testing Complete API Workflow")
        print("=" * 50)
        
        # 1. Health Check
        print("\n1. Testing Health Check...")
        response = client.get('/api/health')
        print(f"   Status: {response.status_code}")
        print(f"   Response: {response.get_json()}")
        assert response.status_code == 200
        
        # 2. Create realistic support dump
        print("\n2. Creating realistic support dump...")
        zip_path = create_realistic_support_dump()
        print(f"   Created: {zip_path}")
        
        # 3. Upload File
        print("\n3. Testing File Upload...")
        with open(zip_path, 'rb') as f:
            response = client.post('/api/upload', data={
                'support_dump': (f, 'realistic_support_dump.zip')
            })
        
        print(f"   Status: {response.status_code}")
        upload_data = response.get_json()
        print(f"   Response: {upload_data}")
        assert response.status_code == 200
        session_id = upload_data['session_id']
        
        # 4. Trigger Analysis
        print(f"\n4. Testing Analysis (Session: {session_id[:8]}...)...")
        response = client.post(f'/api/analyze/{session_id}', 
                             json={'log_level': 'INFO'})
        
        print(f"   Status: {response.status_code}")
        analysis_data = response.get_json()
        print(f"   Response: {analysis_data}")
        
        if response.status_code == 200:
            # 5. Get Results
            print("\n5. Testing Results Retrieval...")
            response = client.get(f'/api/results/{session_id}')
            
            print(f"   Status: {response.status_code}")
            if response.status_code == 200:
                results = response.get_json()
                print(f"   Summary: {results.get('summary', {})}")
                print(f"   Log entries found: {len(results.get('logs', []))}")
            else:
                print(f"   Error: {response.get_json()}")
        else:
            print(f"   Analysis failed: {analysis_data}")
        
        # 6. List Sessions
        print("\n6. Testing Session List...")
        response = client.get('/api/sessions')
        sessions_data = response.get_json()
        print(f"   Active sessions: {sessions_data['active_sessions']}")
        
        # 7. Cleanup
        print(f"\n7. Testing Cleanup...")
        response = client.delete(f'/api/sessions/{session_id}')
        print(f"   Cleanup status: {response.status_code}")
        
        print("\n✅ Complete API workflow test finished!")

if __name__ == '__main__':
    test_complete_workflow()
