from domain.pedido import Pedido

class PedidoService:
    def __init__(self, repository):
        self.repository = repository

    def create_pedido(self, id_pedido: str, id_usuario: str, total: float):
        nuevo_pedido = Pedido(id_pedido=id_pedido, id_usuario=id_usuario, total=total)
        return self.repository.save(nuevo_pedido)

    def get_pedido(self, id_pedido: str):
        return self.repository.get_by_id(id_pedido)

    def update_pedido(self, id_pedido: str, total: float):
        return self.repository.update(id_pedido, {"total": total})

    def delete_pedido(self, id_pedido: str):
        return self.repository.delete(id_pedido)