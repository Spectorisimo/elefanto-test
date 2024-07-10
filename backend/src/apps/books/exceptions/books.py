from dataclasses import dataclass

from src.apps.common.exceptions import ServiceException


@dataclass(eq=False)
class BookNotFoundException(ServiceException):
    book_id: int

    @property
    def message(self):
        return f'Book with id {self.book_id} not found'
