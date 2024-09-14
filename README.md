# Document Retrieval System

## Overview

This project implements a Document Retrieval System for chat applications, designed to fetch and rank documents based on query input. The backend is built using FastAPI and containerized with Docker for easy deployment.

## Features

- Fast document retrieval with text similarity search
- Caching with Redis for faster query responses
- Rate limiting to restrict excessive API usage (HTTP 429 after 5 requests)
- Background scraping of news articles
- Dockerized for quick and scalable deployment

## Setup Instructions

### 1. Local Setup

1. **Install dependencies:**
   
pip install -r requirements.txt

2. **Initialize the database:**

python -c "from app.models import init_db; init_db()"

3. **Run the FastAPI server:**

uvicorn app.api:app --reload

Access the API:

- Health check: http://localhost:8000/health
- API docs: http://localhost:8000/docs

### 2. Docker Setup

1. Build the Docker image:

docker build -t document-retrieval .

2. Run the Docker container:

docker run -p 8000:8000 document-retrieval

### 3. Design Choices

- FastAPI: For high performance and auto-generated documentation
- SQLite: For simplicity; can be switched to PostgreSQL for production
- Redis: For caching and optimization

## Collaborator
- Add recruitments@trademarkia.com as a collaborator
