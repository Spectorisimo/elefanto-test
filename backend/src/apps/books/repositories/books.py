from abc import ABC, abstractmethod

from django.db.models import Q

from src.apps.books.exceptions.books import BookNotFoundException
from src.apps.books.filters.books import BookFilters
from src.apps.books.models import BookModel
from src.apps.books.entities.books import Book


class BaseBookRepository(ABC):

    @abstractmethod
    def get_book(self, book_id: int) -> Book:
        ...

    @abstractmethod
    def get_book_list(self, filters: BookFilters) -> list[Book]:
        ...


class ORMBookRepository(BaseBookRepository):

    def get_book(self, book_id: int) -> Book:
        book = BookModel.objects.filter(id=book_id)
        if not book:
            raise BookNotFoundException(book_id=book_id)
        return book.first().to_entity()

    def get_book_list(self, filters: BookFilters) -> list[Book]:
        query = self._build_product_query(filters)
        book_list = BookModel.objects.filter(query).select_related('genre', 'author').prefetch_related('favorites')
        return [book.to_entity() for book in book_list]

    def _build_product_query(self, filters: BookFilters) -> Q:
        query = Q(is_visible=True)

        if filters.author_id:
            query &= Q(author__id=filters.author_id)

        if filters.genre_id:
            query &= Q(author__id=filters.genre_id)

        if filters.publication_date__lte:
            query &= Q(publication_date__lte=filters.publication_date__lte)

        if filters.publication_date__gte:
            query &= Q(publication_date__gte=filters.publication_date__gte)

        return query
