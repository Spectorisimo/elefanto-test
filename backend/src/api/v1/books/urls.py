from django.urls import path

from src.api.v1.books.views import BookAPIView

urlpatterns = [
    path('', BookAPIView.as_view(
        {'get': 'list'}
    )),
    path('<int:book_id>/', BookAPIView.as_view(
        {'get': 'retrieve'}
    )),
]
