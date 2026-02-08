from pydantic import BaseModel
from enum import Enum
from typing import Optional

class UserStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"

class User(BaseModel):
    """Entidad de dominio: User"""
    idusuario: str
    nombre: str
    email: str
    status: UserStatus = UserStatus.ACTIVE

    # Comportamientos de dominio (como en la foto de clase)
    def activate(self):
        self.status = UserStatus.ACTIVE
        
    def deactivate(self):
        self.status = UserStatus.INACTIVE


class UserCreate(BaseModel):
    """DTO para crear usuario"""
    idusuario: str
    nombre: str
    email: str

class UserUpdate(BaseModel):
    """DTO para actualizar usuario"""
    nombre: Optional[str] = None
    email: Optional[str] = None