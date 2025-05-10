FROM --platform=linux/amd64 python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Use Gunicorn as production server
RUN pip install gunicorn==20.1.0
EXPOSE 8080

# Run with 4 worker processes
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "4", "app.main:app"]