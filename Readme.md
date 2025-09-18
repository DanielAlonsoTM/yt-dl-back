# YT-DL-BACKEND

A backend service for managing YouTube downloads.

---

## 📋 Requirements
- Python **3.x**
- Docker (optional, for containerized execution)

---

## 🚀 Running Locally (without Docker)

### 1. Create and activate a virtual environment
```bash
# Install virtualenv if you don't have it
pip install virtualenv

# Create a virtual environment
virtualenv venv

# Activate the virtual environment
# macOS / Linux
source venv/bin/activate

# Windows (PowerShell)
.\venv\Scripts\activate
```
### 2.  Install dependencies
pip install -r requirements.txt

---

## 🐳 Running with Docker
```bash
# Build the Docker image
docker build -t yt-dl-back .

# Run the container
docker run -p 5000:5000 yt-dl-back
```

---

## 📦 Publishing the Image
```bash
# Build the image with your Docker Hub username
docker build -t <DOCKER_USER>/yt-dl-back .

# Push the image
docker push <DOCKER_USER>/yt-dl-back
```
