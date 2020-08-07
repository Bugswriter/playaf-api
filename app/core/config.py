import secrets
from typing import Any, Dict, List, Optional, Union
from pydantic import AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, PostgresDsr, validator

class Settings(BaseSettings):
    API_V1_STR:  str = "/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    PROJECT_NAME: str = "PlayAF API"
    FIRST_SUPERUSER: str = "suraj@bugswriter.com"
    FIRST_SUPERUSER_PASSWORD: str = "mytestpassword"
    class Config:
        case_sensitive = True


settings = Settings()
