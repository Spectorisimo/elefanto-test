from dataclasses import dataclass
from abc import ABC, abstractmethod

from src.apps.books.entities.books import Book
from src.apps.books.filters.books import BookFilters
from src.apps.books.repositories.books import BaseBookRepository


@dataclass
class BaseBookServices(ABC):

    @abstractmethod
    def get_book(self, book_id: int) -> Book:
        ...

    @abstractmethod
    def get_book_list(self, filters: BookFilters) -> list[Book]:
        ...


@dataclass
class BookServices(BaseBookServices):
    book_repo: BaseBookRepository

    def get_book(self, book_id: int) -> Book:
        return self.book_repo.get_book(book_id)

    def get_book_list(self, filters: BookFilters) -> list[Book]:
        return self.book_repo.get_book_list(filters)
