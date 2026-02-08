from pydantic import BaseModel
from datetime import datetime

class Pedido(BaseModel):
    """Entidad de dominio: Pedido"""
    id_pedido: str
    id_usuario: str  # Relación con el usuario
    total: float
    fecha: datetime = datetime.now()