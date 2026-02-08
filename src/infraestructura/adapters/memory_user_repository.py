from typing import List, Optional
from src.application.ports.user_repository import UserRepository
from src.domain.user import User, UserUpdate

class MemoryUserRepository(UserRepository):
    def __init__(self):
        # Diccionario para guardar usuarios en RAM
        self._users = {}

    def save(self, user: User) -> User:
        self._users[user.idusuario] = user
        return user

    def find_by_id(self, user_id: str) -> Optional[User]:
        return self._users.get(user_id)

    def find_all(self) -> List[User]:
        return list(self._users.values())

    def update(self, user_id: str, user_data: UserUpdate) -> Optional[User]:
        if user_id in self._users:
            user = self._users[user_id]
            # Solo actualizamos si los valores no son None (como en la lógica de la clase)
            if user_data.nombre:
                user.nombre = user_data.nombre
            if user_data.email:
                user.email = user_data.email
            self._users[user_id] = user
            return user
        return None

    def delete(self, user_id: str) -> bool:
        if user_id in self._users:
            del self._users[user_id]
            return True
        return False