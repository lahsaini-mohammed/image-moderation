import os
import requests
from PIL import Image
import io
from .image_analysis import analyze_image
from .content_safety import check_content_safety

def load_api_key():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not found in environment variables")
    return api_key

def process_image(image, url):
    api_key = load_api_key()

    if image is not None:
        analysis = analyze_image(image, api_key)
        safety_check = check_content_safety(analysis, api_key)
        return analysis, safety_check
    elif url:
        try:
            response = requests.get(url)
            image = Image.open(io.BytesIO(response.content))
            analysis = analyze_image(url, api_key, is_url=True)
            safety_check = check_content_safety(analysis, api_key)
            return analysis, safety_check
        except Exception:
            return f"Error processing image URL", ""
    else:
        return "Please provide an image to analyze.", ""