from abc import (
    ABC,
    abstractmethod,
)

from src.apps.users.entities.users import User


class BaseSenderService(ABC):
    @abstractmethod
    def send_code(self, user: User, code: str) -> None:
        ...


class EmailSenderService(BaseSenderService):
    def send_code(self, user: User, code: str) -> None:
        print(f'sent code {code} to user email: customeremail')
