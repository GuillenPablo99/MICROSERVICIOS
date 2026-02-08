from typing import List, Optional
from src.application.ports.user_repository import UserRepository
from src.domain.user import User, UserUpdate

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create_user(self, idusuario: str, nombre: str, email: str) -> User:
        user = User(idusuario=idusuario, nombre=nombre, email=email)
        return self.repository.save(user)

    def get_user(self, user_id: str) -> Optional[User]:
        return self.repository.find_by_id(user_id)

    def get_all_users(self) -> List[User]:
        return self.repository.find_all()

    def update_user(self, user_id: str, user_data: UserUpdate) -> Optional[User]:
        return self.repository.update(user_id, user_data)

    def delete_user(self, user_id: str) -> bool:
        return self.repository.delete(user_id)