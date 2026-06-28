import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Create client
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# Send a simple prompt
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Say hello to FactoryOps AI in one sentence."
)

print(response.text)