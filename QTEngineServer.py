import sys
import os

# Add the QTEngine directory to Python path
current_dir = os.path.dirname(__file__)
qt_engine_path = os.path.join(current_dir, 'QTEngine')
sys.path.append(qt_engine_path)
os.chdir(qt_engine_path)  # Change working directory to QTEngine folder

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from QTEngine import QTEngine

# Initialize FastAPI app
app = FastAPI(
    title="QTEngine Translation API",
    description="API for Chinese to Sino-Vietnamese translation using QTEngine",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Initialize QTEngine
qt_engine = QTEngine()

class TranslationRequest(BaseModel):
    text: str
    options: Optional[dict] = None

class TranslationResponse(BaseModel):
    translated_text: str
    metadata: Optional[dict] = None

@app.get("/")
async def root():
    """Root endpoint returning API information"""
    return {
        "name": "QTEngine Translation API",
        "version": "1.0.0",
        "status": "active"
    }

@app.get("/ping")
async def ping():
    """Endpoint to check server availability"""
    return {
        "status": "ok",
        "message": "Server is running and available"
    }

@app.post("/translate", response_model=TranslationResponse)
async def translate(request: TranslationRequest):
    """
    Translate Chinese text to Sino-Vietnamese
    
    Args:
        request: TranslationRequest containing text to translate
        
    Returns:
        TranslationResponse containing translated text and metadata
    """
    try:
        # Perform translation
        translated_text = qt_engine.translate(request.text)
        
        # Get simplified metadata
        metadata = {
            'status': 'success',
            'source_length': len(request.text),
            'translated_length': len(translated_text)
        }
        
        return TranslationResponse(
            translated_text=translated_text,
            metadata=metadata
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/metadata")
async def get_metadata():
    """Get translation engine metadata"""
    try:
        return qt_engine.get_translation_metadata()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=2210)
