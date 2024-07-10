from django.db import models

from src.apps.books.entities.books import Genre, Author, Book
from src.apps.common.models import BaseDateTimeModel
from django.utils.translation import gettext_lazy as _


class GenreModel(BaseDateTimeModel):
    name = models.CharField(max_length=255, verbose_name=_('Name'))

    def __str__(self):
        return self.name

    @classmethod
    def from_entity(cls, genre_entity: Genre) -> 'GenreModel':
        return cls(
            id=genre_entity.id,
            name=genre_entity.name,
        )

    def to_entity(self) -> Genre:
        return Genre(
            id=self.id,
            name=self.name,
        )

    class Meta:
        verbose_name = _('Genre')
        verbose_name_plural = _('Genres')


class AuthorModel(BaseDateTimeModel):
    first_name = models.CharField(max_length=255, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=255, verbose_name=_('Last Name'))

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = _('Author')
        verbose_name_plural = _('Authors')

    @classmethod
    def from_entity(cls, author_entity: Author) -> 'AuthorModel':
        return cls(
            id=author_entity.id,
            first_name=author_entity.first_name,
            last_name=author_entity.last_name,
        )

    def to_entity(self) -> Author:
        return Author(
            id=self.id,
            first_name=self.first_name,
            last_name=self.last_name,
        )


class BookModel(BaseDateTimeModel):
    title = models.CharField(max_length=255, verbose_name=_('Title'))

    genre = models.ForeignKey(GenreModel, on_delete=models.CASCADE, related_name='books', verbose_name=_('Genre'))
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE, related_name='books', verbose_name=_('Author'))

    publication_date = models.DateField(verbose_name=_('Publication Date'))
    description = models.TextField(verbose_name=_('Description'))

    favorites = models.ManyToManyField('users.UserModel', related_name='favorite_books', blank=True,
                                       verbose_name=_('Favorites'))
    is_visible = models.BooleanField(default=True, verbose_name=_('Is visible'))

    @classmethod
    def from_entity(cls, book_entity: Book) -> 'BookModel':
        return BookModel(
            id=book_entity.id,
            genre=GenreModel.from_entity(book_entity.genre),
            author=AuthorModel.from_entity(book_entity.author),
            publication_date=book_entity.publication_date,
            description=book_entity.description,
        )

    def to_entity(self) -> Book:
        return Book(
            id=self.id,
            title=self.title,
            genre=self.genre.to_entity(),
            author=self.author.to_entity(),
            publication_date=self.publication_date,
            description=self.description,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Book')
        verbose_name_plural = _('Books')
