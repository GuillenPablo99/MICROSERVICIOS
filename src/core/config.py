from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Sistema Restaurante Hexagonal"
    
    user_service_port: int = 8001
    pedido_service_port: int = 8002
    
    debug: bool = True

    class Config:
        env_file = ".env"

settings = Settings()