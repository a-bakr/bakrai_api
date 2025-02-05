# Use multi-stage build to minimize final image size
FROM python:3.10-slim as builder

WORKDIR /app

# Install only essential system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# Install packages to user directory
RUN pip install --user --no-cache-dir -r requirements.txt

# Final stage
FROM python:3.10-slim

WORKDIR /app

# Copy only necessary files from builder
COPY --from=builder /root/.local /root/.local
COPY . .

# Ensure user-installed packages are in PATH
ENV PATH=/root/.local/bin:$PATH

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]