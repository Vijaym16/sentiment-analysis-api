from textblob import TextBlob

def analyze_text_sentiment(text: str):
    """
    Analyzes the sentiment of a given string using TextBlob.
    Returns a dictionary with score, label, and subjectivity.
    """
    blob = TextBlob(text)
    
    polarity = blob.sentiment.polarity
    
    # Logic to determine the human-readable label
    if polarity > 0.1:
        label = "Positive"
    elif polarity < -0.1:
        label = "Negative"
    else:
        label = "Neutral"
        
    return {
        "score": round(polarity, 2),
        "label": label,
        "subjectivity": round(blob.sentiment.subjectivity, 2)
    }