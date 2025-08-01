# gunicorn.conf.py
"""Gunicorn configuration for production deployment."""

import os

# Server socket
bind = f"0.0.0.0:{os.environ.get('PORT', 5000)}"
backlog = 2048

# Worker processes
workers = int(os.environ.get('GUNICORN_WORKERS', 2))
worker_class = 'sync'
worker_connections = 1000
timeout = 30
keepalive = 2

# Restart workers after this many requests, to help prevent memory leaks
max_requests = 1000
max_requests_jitter = 100

# Security
limit_request_line = 4094
limit_request_fields = 100
limit_request_field_size = 8190

# Logging
loglevel = os.environ.get('LOG_LEVEL', 'info').lower()
accesslog = '-'
errorlog = '-'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(D)s'

# Process naming
proc_name = 'rocketchat-analyzer'

# Server mechanics
preload_app = True
daemon = False
pidfile = None
user = None
group = None
tmp_upload_dir = None

# SSL (if needed)
# keyfile = None
# certfile = None
