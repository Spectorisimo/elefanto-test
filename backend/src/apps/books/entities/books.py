from dataclasses import dataclass, field
from datetime import datetime, date


@dataclass
class Genre:
    id: int | None = field(default=None, kw_only=True)  # noqa

    name: str


@dataclass
class Author:
    id: int | None = field(default=None, kw_only=True)  # noqa

    first_name: str
    last_name: str


@dataclass
class Book:
    id: int | None = field(default=None, kw_only=True)  # noqa

    title: str
    genre: Genre
    author: Author

    publication_date: date
    description: str

    created_at: datetime
    updated_at: datetime | None = field(default=None)
