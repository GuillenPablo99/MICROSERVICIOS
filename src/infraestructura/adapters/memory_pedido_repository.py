from typing import List, Optional
from application.ports.pedido_repository import PedidoRepository
from domain.pedido import Pedido

class MemoryPedidoRepository(PedidoRepository):
    def __init__(self):
        self._pedidos = {}

    def save(self, pedido: Pedido) -> Pedido:
        self._pedidos[pedido.id_pedido] = pedido
        return pedido

    def find_by_id(self, pedido_id: str) -> Optional[Pedido]:
        return self._pedidos.get(pedido_id)

    def find_all(self) -> List[Pedido]:
        return list(self._pedidos.values())

    def delete(self, pedido_id: str) -> bool:
        if pedido_id in self._pedidos:
            del self._pedidos[pedido_id]
            return True
        return False