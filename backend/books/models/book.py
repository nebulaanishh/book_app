from django.contrib.auth import get_user_model
from django.db import models

from books.models.base import BaseModel


class Book(BaseModel):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to="book_covers/")
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="books"
    )

    def __str__(self) -> str:
        return self.title

    @classmethod
    def get_all_books(cls):
        books = cls.objects.all()
        return books

    @classmethod
    def get_book_by_idx(cls, idx: str):
        book = cls.objects.get(idx=idx)
        return book

    @classmethod
    def get_book_by_title(cls, title: str):
        book = cls.objects.get(title=title)
        return book
