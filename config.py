from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name : str = "JalenOS"
    database_url : str
    
    model_config = SettingsConfigDict(env_file=".env")