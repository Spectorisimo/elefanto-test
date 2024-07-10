from dataclasses import dataclass

from src.apps.books.entities.books import Book


@dataclass
class User:
    id: int | None = field(default=None, kw_only=True)  # noqa

    email: str

    first_name: str
    last_name: str

    favorite_books: list[Book]
