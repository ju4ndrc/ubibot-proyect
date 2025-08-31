from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    api_key : str;
    channel_id : str;
    base_url : str;

    class Config:
        env_file = ".env";

settings = Settings();