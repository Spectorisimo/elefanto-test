from django.db import models

from src.apps.common.models import BaseDateTimeModel


class ReviewModel(BaseDateTimeModel):
    book = models.ForeignKey('books.BookModel', related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey('users.UserModel', related_name='reviews', on_delete=models.CASCADE)
    rating = models.IntegerField()
    text = models.TextField()

    class Meta:
        verbose_name = 'Book review'
        verbose_name_plural = 'Book reviews'
        unique_together = (
            ('user', 'book'),
        )
