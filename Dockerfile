# Use a Python image
FROM python:3.9-slim

# Install wkhtmltopdf dependencies
RUN apt-get update && \
    apt-get install -y wkhtmltopdf && \
    apt-get clean

# Set up the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Expose the Flask app port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
