from fastapi import APIRouter, HTTPException
from domain.pedido import Pedido
from application.services.pedido_service import PedidoService
from infraestructura.adapters.memory_pedido_repository import MemoryPedidoRepository

router = APIRouter()
pedido_repo = MemoryPedidoRepository()
pedido_service = PedidoService(pedido_repo)

@router.post("/pedidos/", response_model=Pedido)
def crear_pedido(pedido: Pedido):
    return pedido_service.create_pedido(pedido.id_pedido, pedido.id_usuario, pedido.total)

@router.get("/pedidos/{id_pedido}", response_model=Pedido)
def obtener_pedido(id_pedido: str):
    pedido = pedido_service.get_pedido(id_pedido)
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return pedido