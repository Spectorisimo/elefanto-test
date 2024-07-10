from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from src.api.v1.books.serializers import BookSerializer
from src.apps.books.filters.books import BookFilters
from src.apps.books.services.books import BaseBookServices
from src.apps.common.exceptions import ServiceException
from src.config.containers import get_container


class BookAPIView(GenericViewSet):
    container = get_container()
    serializer_class = BookSerializer
    book_services: BaseBookServices = container.resolve(BaseBookServices)

    def list(self, request):
        book_list = self.book_services.get_book_list(BookFilters(**self.request.query_params.dict()))
        serializer = self.serializer_class(book_list, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, book_id: int = None):
        try:
            book = self.book_services.get_book(book_id)
        except ServiceException as e:
            return Response(data={'detail': e.message}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.serializer_class(instance=book)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
