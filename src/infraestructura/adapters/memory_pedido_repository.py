from domain.pedido import Pedido

class MemoryPedidoRepository:
    def __init__(self):
        self.pedidos = []

    def save(self, pedido: Pedido):
        self.pedidos.append(pedido)
        return pedido

    def get_by_id(self, id_pedido: str):
        return next((p for p in self.pedidos if p.id_pedido == id_pedido), None)

    def update(self, id_pedido: str, datos_nuevos: dict):
        pedido = self.get_by_id(id_pedido)
        if pedido:
            pedido.total = datos_nuevos.get("total", pedido.total)
            return pedido
        return None

    def delete(self, id_pedido: str):
        pedido = self.get_by_id(id_pedido)
        if pedido:
            self.pedidos.remove(pedido)
            return True
        return False