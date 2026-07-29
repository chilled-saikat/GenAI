from google import genai
from config import API

client=genai.Client(api_key=API)

response = client._models.generate_content(
    model="gemini-3.5-flash",
    contents="What is Python"
)
print(response.text)