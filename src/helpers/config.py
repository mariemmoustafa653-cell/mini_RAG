from pydantic_settings import BaseSettings ,SettingsConfigDict

class settings(BaseSettings):
    app_name:str
    app_version:str
    OPENAI_API_KEY:str
    
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
def get_settings():
    return settings()