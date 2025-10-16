# Use a lightweight Python image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy all files from your folder to /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run your Python script
CMD ["python", "app.py"]
