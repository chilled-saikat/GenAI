from google import genai
from config import API

client=genai.Client(api_key=API)

print("==========="*50)
print("This is Gemini Powered Chatbot")
print("\nIf you want to exit the chatbot then AI CHATBOT EXIT")
print("==========="*50)

while True:
    user_input = input("\nYou Question: ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=user_input
    )

    print("Bot Answer:" ,response.text)