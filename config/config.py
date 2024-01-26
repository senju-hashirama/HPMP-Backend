import os
from dotenv import load_dotenv
import json

load_dotenv(".env.dev")


def get_settings():
    ENV_NAME = os.environ.get("ENV_NAME")

    BASE_URL = os.environ.get("BASE_URL")

    DB_URL = os.environ.get("DB_URL")

    DB_PASSWORD = os.environ.get("DB_PASSWORD")

    FIREBASE_CONFIG = json.loads(os.environ.get("FIREBASE_CONFIG"))
    return {"ENV_NAME":ENV_NAME,"BASE_URL":BASE_URL,"DB_URL":DB_URL,"DB_PASSWORD":DB_PASSWORD,"FIREBASE_CONFIG":FIREBASE_CONFIG}


