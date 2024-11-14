from rest_framework.generics import ListAPIView, RetrieveAPIView
from books.models import Book
from books.serializers import BookSerializer
from books.filters import BookFilter



class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_class = BookFilter
    search_fields = ['title', 'authors__first_name', 'authors__last_name']

class BookDetailView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
