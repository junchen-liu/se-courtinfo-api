import os

PROJECT_NAME = "Suffolk County District Attorney API"

SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

API_V1_STR = "/api/v1"
