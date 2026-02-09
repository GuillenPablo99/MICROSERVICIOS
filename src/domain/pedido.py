from pydantic import BaseModel
from datetime import datetime

class Pedido(BaseModel):
    """Entidad de dominio: Pedido"""
    id_pedido: str
    id_usuario: str 
    total: float
    fecha: datetime = datetime.now()