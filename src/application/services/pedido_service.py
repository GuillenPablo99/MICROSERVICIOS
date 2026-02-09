from typing import List, Optional
from application.ports.pedido_repository import PedidoRepository
from domain.pedido import Pedido

class PedidoService:
    def __init__(self, repository: PedidoRepository):
        self.repository = repository

    def create_pedido(self, id_pedido: str, id_usuario: str, total: float) -> Pedido:
        pedido = Pedido(id_pedido=id_pedido, id_usuario=id_usuario, total=total)
        return self.repository.save(pedido)

    def get_pedido(self, pedido_id: str) -> Optional[Pedido]:
        return self.repository.find_by_id(pedido_id)

    def get_all_pedidos(self) -> List[Pedido]:
        return self.repository.find_all()

    def delete_pedido(self, pedido_id: str) -> bool:
        return self.repository.delete(pedido_id)