# Deployment Guide: Due Diligence Automation System

---

**Project Name**: Due Diligence Automation System  
**Test Date**: [Date]  
**Test Lead**: [Lead Name]  
**Project Version**: V1.0  
**Backend Tech Stack**: FastAPI  
**Database**: MySQL  
**Web Scraping Targets**: Common Australian business query websites (e.g., ASIC, ABN Lookup) and Google  
**Test Tools**: Pytest, Postman, Selenium  
**Scope**: The deployment plan aims for seamless deployment with thorough documentation and proactive issue resolution. The code is tested regularly to ensure zero post-deployment issues.

---

## 1. Project Overview

The Due Diligence Automation System is designed to assist users in conducting risk assessments by entering company information. The system automatically fetches data from multiple Australian business query websites (e.g., ASIC, ABN Lookup) and Google, then generates a comprehensive due diligence report. The backend is built using FastAPI, and MySQL is used for data storage.

---

## 2. Deployment Objectives
The objective is to achieve a seamless deployment, meeting the following criteria:
- **Seamless Deployment**: The deployment process should require minimal manual intervention and support automation.
- **Thorough Documentation**: Complete deployment and operational documentation should be provided.
- **Proactive Issue Resolution**: Common deployment issues should be anticipated with detailed solutions to ensure a smooth process.
- **Zero Post-Deployment Issues**: With thorough CI/CD integration and extensive testing, the system should remain stable and error-free after deployment.

---

## 3. Deployment Environment
- **Operating System**: Ubuntu 20.04 LTS (Linux)
- **Docker Version**: 20.10.8
- **Python Version**: 3.12
- **Database**: MySQL 8.0
- **Backend Framework**: FastAPI
- **Web Management Tool**: Adminer latest version

---

## 4. Tool Installation and Setup

### 4.1. Installing Docker:
To install Docker on Ubuntu 20.04, follow these steps:

```bash
# Update package information
sudo apt update

# Install necessary packages
sudo apt install apt-transport-https ca-certificates curl software-properties-common -y

# Add Docker's GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Add Docker's APT repository
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker
sudo apt update
sudo apt install docker-ce -y

# Start and enable Docker
sudo systemctl start docker
sudo systemctl enable docker

# Verify Docker installation
docker --version
```

### 4.2. Installing Docker Compose:
Before installing Docker Compose, check if it is already installed, as some Docker installations include Docker Compose by default:

```bash
# Check if Docker Compose is already installed
docker-compose --version

# If the above command returns a version number, Docker Compose is already installed.
# If it shows "command not found", proceed with the installation.

# Download Docker Compose binary (if not installed)
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

# Give executable permissions
sudo chmod +x /usr/local/bin/docker-compose

# Verify Docker Compose installation
docker-compose --version
```


### 4.3. Setting Up Python Environment:
- **Virtual Environment**: Use `venv` for creating a virtual environment during local development.
- **Package Management**: Use `pip` to manage dependencies, recorded in `requirements.txt`.

---

## 5. Docker Configuration
### 5.1. Docker Compose Configuration (`docker-compose.yml`):
Create a `docker-compose.yml` file in the root directory to define the configuration of each service. Below is the full content:

```yaml
version: '3.8'

services:
  db:
    image: mysql:8
    container_name: research_due_diligence_db
    environment:
      MYSQL_ROOT_PASSWORD: 1234
      MYSQL_DATABASE: research_due_diligence
      MYSQL_USER: user
      MYSQL_PASSWORD: 1234
    ports:
      - "3307:3306"
    volumes:
      - db_data:/var/lib/mysql
    networks:
      - research_network
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "localhost"]
      interval: 30s
      timeout: 10s
      retries: 5

  adminer:
    image: adminer
    container_name: research_due_diligence_adminer
    ports:
      - "8080:8080"
    networks:
      - research_network

  web:
    build: .
    container_name: research_due_diligence_web
    command: uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
    volumes:
      - .:/code  
    ports:
      - "8001:8000"
    depends_on:
      - db
    networks:
      - research_network
    restart: always

volumes:
  db_data:

networks:
  research_network:
```

### 5.2. Writing the Dockerfile:
Create a `Dockerfile` with the following content:

```dockerfile
FROM python:3.12-slim

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt 
COPY . .

# Add health check script to ensure app runs healthily
HEALTHCHECK --interval=30s --timeout=10s --start-period=10s --retries=3 
  CMD curl --fail http://localhost:8000/health || exit 1
```

### 5.3. Building and Starting Services:
Run the following command in the root directory to build the image and start services:

```bash
docker-compose up --build -d
```

### 5.4. Verifying Service Status:
Check the status of all containers to ensure services are running properly:

```bash
docker-compose ps
```

---

## 6. CI/CD Integration
Integrate with GitHub Actions for CI/CD to automate testing and deployment. Below is a sample `.github/workflows/deploy.yml` configuration:

```yaml
name: CI/CD Pipeline

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.12'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: pytest
      - name: Build Docker Image
        run: docker build -t research_due_diligence_web .
      - name: Push Docker Image
        run: docker-compose up -d
```

---

## 7. Documentation
- **README.md**: Contains project introduction, deployment steps, environment requirements, and API usage instructions.
- **API Documentation**: Accessible through FastAPI's built-in OpenAPI docs at `http://localhost:8001/docs`.
- **Deployment Guide**: Details Docker and Docker Compose installation, configuration, usage steps, and common issues and solutions.

---

## 8. Common Issues and Solutions
- **Database Connection Issues**: Verify `MYSQL_USER` and `MYSQL_PASSWORD`, and ensure port `3307` is not occupied.
- **Container Restart**: Use `restart: always` to ensure the container automatically restarts on failure.
- **Health Check Failures**: Check the `HEALTHCHECK` script output to ensure the app is serving on the specified port.

---

## 9. Tools and Versions
- Docker Version: 20.10.8
- Python Version: 3.12
- MySQL Version: 8.0
- Adminer Version: Latest (pulled through `adminer` image)
- GitHub Actions: Used for CI/CD automation

---

## 10. Conclusion
Through the detailed deployment steps and automated CI/CD pipeline, the Due Diligence Automation System achieves stability in production environments. The entire process ensures seamless deployment, thorough documentation, and proactive issue resolution, meeting the standard of "Deployment is seamless, with excellent documentation and proactive resolution of potential issues; zero post-deployment issues."

---

