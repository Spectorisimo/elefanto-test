import random
from abc import (
    ABC,
    abstractmethod,
)

from django.core.cache import cache

from src.apps.users.entities.users import User
from src.apps.users.exceptions.codes import (
    CodeNotFoundException,
    CodesNotEqualException,
)


class BaseCodeService(ABC):
    @abstractmethod
    def generate_code(self, customer: User) -> str:
        ...

    @abstractmethod
    def validate_code(self, code: str, customer: User) -> None:
        ...


class DjangoCacheCodeService(BaseCodeService):
    def generate_code(self, user: User) -> str:
        code = str(random.randint(100000, 999999))  # noqa
        cache.set(user.email, code)
        return code

    def validate_code(self, code: str, user: User) -> None:
        cached_code = cache.get(user.email)

        if cached_code is None:
            raise CodeNotFoundException()

        if cached_code != code:
            raise CodesNotEqualException()

        cache.delete(user.email)
