FROM python:3.11-slim

WORKDIR /app

# Copy requirements.txt from project root
COPY ../requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files from root to /app inside container
COPY ../ . 

# Command to run your app
CMD ["python", "main.py"]

