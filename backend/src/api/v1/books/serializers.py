from rest_framework_dataclasses.serializers import DataclassSerializer

from src.apps.books.entities.books import Genre, Author, Book


class GenreSerializer(DataclassSerializer):
    class Meta:
        dataclass = Genre


class AuthorSerializer(DataclassSerializer):
    class Meta:
        dataclass = Author


class BookSerializer(DataclassSerializer):
    class Meta:
        dataclass = Book
