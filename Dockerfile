FROM python:3.11-slim

# Install system tools
RUN apt-get update && apt-get install -y make \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN pip install pytest
# Use official Python slim image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DATABASE_URL="postgresql+psycopg2://chimera:chimera@db:5432/chimera"

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    make \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Default command to run tests
CMD ["pytest", "tests/"]
