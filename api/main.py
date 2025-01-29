from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict
import os

# Create FastAPI instance
app = FastAPI(
    title="Lab Demo API",
    description="Simple FastAPI application with health check"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check() -> Dict[str, str]:
    """
    Health check endpoint to verify the service is running
    """
    return {"status": "healthy", "message": "Service is running! All good!!!"}

@app.get("/")
async def root() -> Dict[str, str]:
    """
    Root endpoint with basic service information
    """
    return {
        "service": "Lab Demo API",
        "version": "1.0.0",
        "documentation": "/docs"
    }

@app.get("/env-demo")
async def get_demo_env() -> Dict[str, str]:
    """
    Demo endpoint that returns an environment variable
    """
    demo_value = os.getenv("DEMO_VALUE", "default_value")
    return {"env_variable": "DEMO_VALUE", "value": demo_value}

@app.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)) -> Dict[str, str]:
    """
    Endpoint to upload a PDF file.

    Returns metadata about the uploaded file.
    """
    # Here, you can add logic to process the PDF file as needed.
    # e.g., saving it to disk, extracting text, storing in a database, etc.

    # For demonstration, we'll just return its metadata.
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "message": "PDF uploaded successfully!"
    }