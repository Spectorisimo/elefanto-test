from functools import lru_cache

import punq

from src.apps.books.repositories.books import ORMBookRepository, BaseBookRepository
from src.apps.books.services.books import BookServices, BaseBookServices


@lru_cache(1)
def get_container() -> punq.Container:
    return _initialize_container()


def _initialize_container() -> punq.Container:
    container = punq.Container()

    container.register(BaseBookRepository, ORMBookRepository)
    container.register(BaseBookServices, BookServices)

    return container
