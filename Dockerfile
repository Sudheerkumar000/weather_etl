# 1. Base image
FROM python:3.11-slim

# 2. Set working directory
WORKDIR /app

# 3. Copy requirements file
COPY requirements.txt .

# 4. Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy all source code into container
COPY . .

# 6. Run main.py on container start
CMD ["python", "main.py"]
