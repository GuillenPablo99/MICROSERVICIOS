from fastapi import APIRouter, HTTPException
from domain.pedido import Pedido
from application.services.pedido_service import PedidoService
from infraestructura.adapters.memory_pedido_repository import MemoryPedidoRepository
from pydantic import BaseModel

class PedidoUpdate(BaseModel):
    total: float

router = APIRouter()
pedido_repo = MemoryPedidoRepository()
pedido_service = PedidoService(pedido_repo)

@router.post("/pedidos/", response_model=Pedido)
def crear_pedido(pedido: Pedido):
    return pedido_service.create_pedido(pedido.id_pedido, pedido.id_usuario, pedido.total)

@router.get("/pedidos/{id_pedido}", response_model=Pedido)
def obtener_pedido(id_pedido: str):
    res = pedido_service.get_pedido(id_pedido)
    if not res:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return res

@router.put("/pedidos/{id_pedido}", response_model=Pedido)
def actualizar_pedido(id_pedido: str, datos: PedidoUpdate):
    res = pedido_service.update_pedido(id_pedido, datos.total)
    if not res:
        raise HTTPException(status_code=404, detail="Pedido no encontrado para actualizar")
    return res

@router.delete("/pedidos/{id_pedido}")
def eliminar_pedido(id_pedido: str):
    exito = pedido_service.delete_pedido(id_pedido)
    if not exito:
        raise HTTPException(status_code=404, detail="No se pudo eliminar el pedido")
    return {"message": f"Pedido {id_pedido} eliminado correctamente"}