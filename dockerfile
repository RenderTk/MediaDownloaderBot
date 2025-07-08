FROM python:3.12.11-alpine3.22

# Install system dependencies (if needed for your requirements)
RUN apk add --no-cache ffmpeg

# Create non-root user
RUN addgroup -S app && adduser -S -G app app

# Set working directory
WORKDIR /app

# Create media directory with proper permissions
RUN mkdir -p /app/media && chown -R app:app /app

# Copy requirements first (for better Docker layer caching)
COPY requirements.txt .

# Switch to non-root user before installing packages
USER app

# Install Python dependencies
RUN pip3 install --no-cache-dir --user -r requirements.txt


# Copy application code
COPY --chown=app:app . .

# Expose port
EXPOSE 8002

# Use CMD instead of ENTRYPOINT for easier overriding
CMD ["python3", "app.py"]