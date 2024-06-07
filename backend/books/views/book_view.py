from rest_framework.views import APIView


from books.service.book_service import BookService
from books.service.review_service import ReviewService
from books.builders.response_builder import ResponseBuilder
from books.helpers.logger_helper import logger


class BookListView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        response_builder = ResponseBuilder()
        try:
            book_service = BookService()
            books = book_service.get_all_book()
            return (
                response_builder.result_object(books).success().ok_200().get_response()
            )
        except Exception as e:
            logger.error(f"BookView get :: exception::  {e}")
            return (
                response_builder.result_object({"message": "Unable to get books"})
                .fail()
                .internal_error_500()
                .message("Internal Error")
                .get_response()
            )


class BookDetailView(APIView):
    def get(self, request, idx, format=None, *args, **kwargs):
        response_builder = ResponseBuilder()
        try:
            book_service = BookService()
            book = book_service.get_book_by_idx(idx)
            reviews = ReviewService.get_reviews_by_book_idx(idx)
            if book:
                return (
                    response_builder.result_object({"book": book, "reviews": reviews})
                    .success()
                    .ok_200()
                    .get_response()
                )
            return (
                response_builder.result_object({"message": "Book not found"})
                .fail()
                .not_found_404()
                .message("Not Found")
                .get_response()
            )

        except Exception as e:
            logger.error(f"BookDetailView get :: exception :: {e}")
            return (
                response_builder.result_object(
                    {"message": "Unable to get book details"}
                )
                .fail()
                .internal_error_500()
                .message("Internal Error")
                .get_response()
            )
