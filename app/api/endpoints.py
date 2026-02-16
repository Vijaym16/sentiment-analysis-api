from fastapi import APIRouter, HTTPException
from app.schemas.sentiment import SentimentRequest, SentimentResponse
from app.services.analyzer import analyze_text_sentiment

# Initialize the router
router = APIRouter()

@router.post("/analyze", response_model=SentimentResponse)
async def analyze_text(request: SentimentRequest):
    """
    Endpoint to analyze text sentiment. 
    It takes a text string and returns polarity and label.
    """
    try:
        # Pass the input text to our AI service
        result = analyze_text_sentiment(request.text)
        return result
    except Exception as e:
        # If something goes wrong, return a 500 error
        raise HTTPException(status_code=500, detail=str(e))