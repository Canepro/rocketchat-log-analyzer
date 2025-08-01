# 🐳 Docker Security & Production Improvements

## Overview
The Dockerfile has been significantly improved for security, performance, and production readiness. It's fully compatible with both Docker and Podman container engines.

## Base Image: Python 3.12 Alpine

We use `python:3.12-alpine` as the base image for several advantages:

- **Smaller Size**: Alpine Linux base (~5MB) vs Debian slim (~40MB)
- **Better Security**: Alpine uses musl libc with fewer attack vectors
- **Latest Python**: Python 3.12 offers performance improvements and latest security patches
- **Faster Builds**: Alpine's `apk` package manager is more efficient than `apt`
- **Production Ready**: Alpine is widely used in production container environments

## Docker & Podman Compatibility

This Dockerfile is fully compatible with both container engines:

### Docker
```bash
docker build -t rocketchat-analyzer .
docker run -p 5000:5000 -e SECRET_KEY=your-key rocketchat-analyzer
```

### Podman
```bash
podman build -t rocketchat-analyzer .
podman run -p 5000:5000 -e SECRET_KEY=your-key rocketchat-analyzer
```

**Note**: Podman uses OCI format by default, so HEALTHCHECK directives show warnings but don't affect functionality.

## Security Improvements

### 1. Non-Root User
- Creates and runs as non-root user `appuser`
- Prevents privilege escalation attacks
- Follows Docker security best practices

### 2. Environment Variables
- Properly configured environment variables for production
- Security-focused defaults
- Configurable resource limits

### 3. System Updates
- Regular security updates applied during build
- Minimal package installation to reduce attack surface

## Production Features

### 1. Gunicorn WSGI Server
- Replaced Flask development server with production-grade Gunicorn
- Configurable workers and performance settings
- Better handling of concurrent requests

### 2. Health Checks
- Built-in Docker health check endpoint
- Automatic container health monitoring
- Proper startup and failure detection

### 3. Resource Management
- Configurable upload and processing limits
- Memory-efficient configuration
- Proper temporary directory handling

## Configuration

### Environment Variables
Set these environment variables when running the container:

```bash
# Required for production
SECRET_KEY=your-secure-secret-key-here

# Optional - File size limits (in bytes)
MAX_UPLOAD_SIZE=104857600         # 100 MB (default)
MAX_EXTRACTED_SIZE=524288000      # 500 MB (default)
MAX_SINGLE_FILE_SIZE=52428800     # 50 MB (default)

# Optional - Gunicorn configuration
GUNICORN_WORKERS=2                # Number of worker processes
PORT=5000                         # Port to bind to
LOG_LEVEL=info                    # Logging level
```

## Usage

### Development
```bash
# Build the image
docker build -t rocketchat-analyzer .

# Run with development settings
docker run -p 5000:5000 -e FLASK_ENV=development rocketchat-analyzer
```

### Production
```bash
# Build the image
docker build -t rocketchat-analyzer .

# Run with production settings
docker run -p 5000:5000 \
  -e SECRET_KEY=your-secure-secret-key \
  -e FLASK_ENV=production \
  -e GUNICORN_WORKERS=4 \
  rocketchat-analyzer
```

### Using Docker Compose (Recommended)
Create a `docker-compose.yml` file:

```yaml
version: '3.8'
services:
  rocketchat-analyzer:
    build: .
    ports:
      - "5000:5000"
    environment:
      - SECRET_KEY=your-secure-secret-key-here
      - FLASK_ENV=production
      - GUNICORN_WORKERS=2
    volumes:
      - ./reports:/app/reports  # Optional: persist reports
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:5000/"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
```

## Security Considerations

1. **Always set SECRET_KEY** in production environments
2. **Use HTTPS** in production with a reverse proxy (nginx, traefik, etc.)
3. **Limit file upload sizes** based on your server capacity
4. **Monitor resource usage** and adjust worker counts accordingly
5. **Keep the container updated** by rebuilding with latest base images

## Performance Tuning

### Worker Configuration
- Start with 2 workers and adjust based on CPU cores and load
- Formula: `(2 × CPU cores) + 1`
- Monitor memory usage per worker

### Resource Limits
- Set appropriate upload limits based on available disk space
- Monitor /app/temp directory usage
- Consider implementing cleanup of old temporary files

## Troubleshooting

### Common Issues
1. **Permission errors**: Ensure proper file permissions for the appuser
2. **Out of memory**: Reduce worker count or increase container memory limits
3. **Upload failures**: Check file size limits and available disk space

### Logging
Container logs can be accessed with:
```bash
docker logs <container-name>
```

Set `LOG_LEVEL=debug` for detailed debugging information.
