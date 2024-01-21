from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    env_name: str = "Local"
    base_url: str = "http://localhost:8000"
    db_url: str = "sqlite:///./shortener.db"
    db_password: str= "test"
    firebase_config: str="a"
    class Config:
        env_file="../.env"

@lru_cache
def get_settings() -> Settings:
    
    settings = Settings()
    return settings
