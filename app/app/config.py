from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = 'mysql://root:root@localhost:3306/test'

    class Config:
        env_file = ".env"
        
settings = Settings()