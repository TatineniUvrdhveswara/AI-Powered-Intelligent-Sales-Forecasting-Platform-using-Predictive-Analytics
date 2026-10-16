import os
from dotenv import load_dotenv
from google import genai

# Load environment variables from .env
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

try:
    if not api_key:
        raise ValueError(
            "GOOGLE_API_KEY not found in your .env file."
        )

    # Initialize the Gemini client
    client = genai.Client(api_key=api_key)

    # Send a test request to Gemini
    response = client.interactions.create(
        model="gemini-3.8-flash",
        input="Say hello"
    )

    # Display the result
    print("✅ Google Gemini API working!")
    print(response.output_text)

except Exception as e:
    print(f"❌ Google Gemini API failed: {e}")