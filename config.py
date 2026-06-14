import os
import sys
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://user:password@localhost/sakhi_db"
    TWILIO_ACCOUNT_SID: str = "MOCK_TWILIO_SID"
    TWILIO_AUTH_TOKEN: str = "MOCK_TWILIO_TOKEN"
    TWILIO_PHONE_NUMBER: str = "+1234567890"
    FIREBASE_CREDENTIALS_PATH: str = "serviceAccountKey.json"

    model_config = SettingsConfigDict(
        env_file=os.path.join(BASE_DIR, ".env"),
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()