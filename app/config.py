from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    ADMIN_EMAIL: str = "bekaxme2007@gmail.com"

    class Config:
        env_file = ".env"



settings = Settings()
