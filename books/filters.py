from books.models import Book
import django_filters


class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label="Title")
    genre = django_filters.NumberFilter(field_name='genre', lookup_expr='exact', label="Genre")
    publication_date = django_filters.DateFilter(field_name='publication_date', lookup_expr='gte', label="Publication Date From")
    authors = django_filters.CharFilter(field_name='authors__full_name', lookup_expr='icontains', label="Authors")

    class Meta:
        model = Book
        fields = ['title', 'genre', 'publication_date', 'authors']