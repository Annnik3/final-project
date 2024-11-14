from django.contrib import admin
from .models import Author, Genre, Book, BookHistory

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')

class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'publication_date', 'quantity')
    list_filter = ('genre',)
    search_fields = ('title', 'authors__first_name', 'authors__last_name')


class BookHistoryAdmin(admin.ModelAdmin):
    list_display = ('book', 'borrower', 'borrow_date', 'return_date')
    list_filter = ('borrower', 'book', 'borrow_date')
    search_fields = ('book__title', 'borrower__username')

admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookHistory, BookHistoryAdmin)
