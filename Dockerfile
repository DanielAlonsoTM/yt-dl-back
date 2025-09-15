# Use the official Python image as a base
FROM python:3.11-slim

# Install dependencies
RUN apt update && apt install -y ffmpeg && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Expose the port your app runs on
EXPOSE 5000

# Command to run the app
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
