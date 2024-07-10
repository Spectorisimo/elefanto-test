from django.contrib import admin

from src.apps.books.models.books import BookModel, GenreModel, AuthorModel


@admin.register(BookModel)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_visible')


@admin.register(GenreModel)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')


@admin.register(AuthorModel)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'created_at', 'updated_at')
