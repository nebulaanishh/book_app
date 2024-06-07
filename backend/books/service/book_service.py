from books.models import Book
from books.serializers.book_serializer import BookSerializer


class BookService:
    def get_all_book(self):
        books = Book.get_all_books()
        return BookSerializer(books, many=True).data

    def get_book_by_idx(self, idx):
        book = Book.get_book_by_idx(idx)
        return BookSerializer(book).data

    def get_book_by_title(self, title: str):
        book = Book.get_book_by_title(title)
        return BookSerializer(book).data
