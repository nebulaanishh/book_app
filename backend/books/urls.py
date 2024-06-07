from django.urls import path
from books.views.book_view import BookListView, BookDetailView

urlpatterns = [
    path("books/", BookListView.as_view(), name="book_list"),
    path("books/<str:idx>/", BookDetailView.as_view(), name="book_detail"),
]
