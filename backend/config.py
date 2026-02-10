import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # Database
    DATABASE_URL: str = "postgresql://aiwg_user:aiwg_password@localhost:5432/ai_website_generator"

    # Hugging Face
    HF_API_TOKEN: str = ""
    HF_MODEL_ID: str = "meta-llama/Llama-2-7b-chat-hf"

    # App
    SECRET_KEY: str = "dev-secret-key"
    DEBUG: bool = True
    CORS_ORIGINS: list[str] = ["http://localhost:5173", "http://localhost:3000"]

    class Config:
        env_file = ".env"


settings = Settings()
