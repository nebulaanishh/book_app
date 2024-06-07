from rest_framework.views import APIView

from books.models import Book, Review
from books.service.book_service import BookService
from books.serializers.book_serializer import BookSerializer

book_service = BookService


class BookListView(APIView):
    def get(self, request, format=None):
        books = book_service.get_all_book()
