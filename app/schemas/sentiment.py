from pydantic import BaseModel, Field

class SentimentRequest(BaseModel):
    text: str = Field(..., min_length=1, example="I like learning AI!")

class SentimentResponse(BaseModel):
    score: float
    label: str
    subjectivity: float