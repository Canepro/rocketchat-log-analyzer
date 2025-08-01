# Use an official Python runtime as a parent image
FROM python:3.12-alpine

# Set environment variables for security and performance
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    FLASK_APP=app.py \
    FLASK_ENV=production \
    SECRET_KEY="" \
    MAX_UPLOAD_SIZE=104857600 \
    MAX_EXTRACTED_SIZE=524288000 \
    MAX_SINGLE_FILE_SIZE=52428800

# Create a non-root user for security
RUN addgroup -g 1001 -S appuser && \
    adduser -S appuser -u 1001 -G appuser

# Set the working directory in the container
WORKDIR /app

# Install system dependencies and security updates
# Alpine uses apk instead of apt-get
RUN apk update && apk add --no-cache \
    curl \
    && apk upgrade \
    && rm -rf /var/cache/apk/*

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies with security considerations
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's code into the container
COPY --chown=appuser:appuser . .

# Create necessary directories and set permissions
RUN mkdir -p /app/temp /app/reports \
    && chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Add health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:5000/ || exit 1

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Use production WSGI server for better performance and security
CMD ["gunicorn", "--config", "gunicorn.conf.py", "app:app"]
