from fastapi import APIRouter, HTTPException
from src.domain.user import User, UserCreate, UserUpdate
from src.application.services.user_service import UserService
from src.infraestructura.adapters.memory_user_repository import MemoryUserRepository

router = APIRouter()

user_repo = MemoryUserRepository()
user_service = UserService(user_repo)

@router.post("/usuarios/", response_model=User)
def crear_usuario(user_data: UserCreate):
    return user_service.create_user(user_data.idusuario, user_data.nombre, user_data.email)

@router.get("/usuarios/{idusuario}", response_model=User)
def obtener_usuario(idusuario: str):
    user = user_service.get_user(idusuario)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

@router.put("/usuarios/{idusuario}", response_model=User)
def actualizar_usuario(idusuario: str, user_data: UserUpdate):
    user = user_service.update_user(idusuario, user_data)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

@router.delete("/usuarios/{idusuario}")
def eliminar_usuario(idusuario: str):
    success = user_service.delete_user(idusuario)
    if not success:
        raise HTTPException(status_code=404, detail="No se pudo eliminar")
    return {"message": "Usuario eliminado correctamente"}