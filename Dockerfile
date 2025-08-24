# Use slim python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies for WeasyPrint
RUN apt-get update && apt-get install -y \
    build-essential \
    libpango-1.0-0 \
    libcairo2 \
    libjpeg62-turbo-dev \
    libpng-dev \
    libgdk-pixbuf2.0-0 \
    libffi-dev \
    shared-mime-info \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Expose ports
EXPOSE 8000 6277

# Default command runs FastAPI + MCP
CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port 8000 & python html2pdf_mcp.py"]
