import os

try:
    from dotenv import load_dotenv
except ImportError:  # pragma: no cover - defensive fallback
    def load_dotenv():
        return False

load_dotenv()
API = os.getenv("API")