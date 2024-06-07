from books.models import Review
from books.service.book_service import BookService


class ReviewService:
    def get_reviews_by_book_idx(self, idx):
        reviews = Review.get_reviews_by_book_idx(idx)
        return reviews
