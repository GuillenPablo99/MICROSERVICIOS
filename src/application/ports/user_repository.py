from abc import ABC, abstractmethod
from typing import List, Optional
from domain.user import User, UserCreate, UserUpdate

class UserRepository(ABC):
    @abstractmethod
    def save(self, user: User) -> User:
        """Define cómo guardar un usuario"""
        pass

    @abstractmethod
    def find_by_id(self, user_id: str) -> Optional[User]:
        """Busca un usuario por ID"""
        pass

    @abstractmethod
    def find_all(self) -> List[User]:
        """Obtiene la lista de todos los usuarios"""
        pass

    @abstractmethod
    def update(self, user_id: str, user_data: UserUpdate) -> Optional[User]:
        """Modifica nombre o email existente"""
        pass

    @abstractmethod
    def delete(self, user_id: str) -> bool:
        """Elimina un usuario del sistema"""
        pass