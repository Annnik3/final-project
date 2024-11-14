from django.db import models
from django.conf import settings


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Book Model
class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField(Author, related_name='books')
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, related_name='books')
    publication_date = models.DateField()
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class BookHistory(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='history')
    borrower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
                                 related_name='borrowed_books')
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.book.title} borrowed by {self.borrower}"
