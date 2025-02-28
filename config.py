from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Vendaval"
    admin_email:str= "rafasaezarana@gmail.com"
    mongo_uri: str
    allowed_origins: [str] 
    model_config = SettingsConfigDict(env_file=".env")