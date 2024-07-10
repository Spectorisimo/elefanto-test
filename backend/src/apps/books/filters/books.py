from dataclasses import dataclass
from datetime import date


@dataclass
class BookFilters:
    author_id: int | None = None
    genre_id: int | None = None

    publication_date__gte: date | None = None
    publication_date__lte: date | None = None
