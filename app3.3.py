import streamlit as st

try:
    from google import genai
except ImportError:  # pragma: no cover - defensive fallback
    genai = None

from config import API

client = None
if genai is not None and API:
    try:
        client = genai.Client(api_key=API)
    except Exception:  # pragma: no cover - defensive fallback
        client = None


def generate_bot_reply(user_input, client_instance=None, retries=2):
    if not user_input or not str(user_input).strip():
        return "Please enter a question before submitting."

    if client_instance is None:
        client_instance = client

    if client_instance is None:
        return "Sorry, the Gemini client is not available. Please check your API configuration and try again."

    models_to_try = ["gemini-2.0-flash", "gemini-1.5-flash"]
    last_error = None

    for attempt in range(retries):
        for model_name in models_to_try:
            try:
                response = client_instance.models.generate_content(
                    model=model_name,
                    contents=user_input,
                )
                reply = getattr(response, "text", None)
                if reply:
                    return reply
                return "Sorry, I could not generate a response right now."
            except Exception as exc:
                last_error = exc
                message = str(exc).lower()
                if "503" in str(exc) or "unavailable" in message or "overload" in message:
                    continue
                return f"Sorry, I could not generate a response right now. Details: {exc}"

    return (
        "Sorry, the Gemini service is temporarily unavailable. "
        f"Please try again in a moment. Details: {last_error}"
    )


def main():
    st.set_page_config(
        page_title="Gemini Powered Chatbot",
        page_icon=":robot:",
        layout="wide",
    )

    st.header("Gemini Powered Chatbot")
    st.write("This is an AI powered chatbot for interaction")
    st.subheader("Input Your Question")

    user_input = st.text_input("Your Question: ")

    if st.button("Enter Your Question"):
        if user_input and user_input.strip():
            with st.spinner("Generating response..."):
                reply = generate_bot_reply(user_input)

            st.subheader("Bot Answer:")
            if reply.startswith("Sorry"):
                st.error(reply)
            else:
                st.success(reply)
        else:
            st.warning("Please enter a question before submitting.")


if __name__ == "__main__":
    main()