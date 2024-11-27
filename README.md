# Library Management System

This is a simple **Library Management System** built with **Django** and **Django REST Framework** that allows users to register, browse, and search books. Admin users can add and manage books, along with their associated genres and authors. The system provides a clean interface for managing book information, and a RESTful API for listing and viewing details of books.

## Features

- **User Registration**: Users can register an account to access the library's books.
- **Admin Panel**: The admin user can:
  - Add and manage books.
  - Add genres and authors as separate models.
  - Filter and search books by title, author name, surname.
  - Search and filter functionality available in Django admin for efficient management.
  - Admin user can also manage book history model in admin panel, Admin user is able to specify which book was borrowed, when and when was it returned to the library.
- **Books List & Detail Endpoints**: 
  - **GET /list/**: List all books with pagination (page number-based).
  - **GET /{id}/**: View details of a specific book.
  - Support for search and filtering by title, author, and genre in the API.

## Models

- **Book**: Contains fields for title, authors (ManyToMany), genre (foreign key), and other book details.
- **Author**: Separate model to manage authors, linked to books.
- **Genre**: Separate model to manage genres, linked to books.
- **BookHistory**: Model for specifing who has borrowed the book and when they returned it.

## API Features

- **Pagination**: The books list endpoint supports pagination based on page numbers.
- **Search**: Users can search for books by title, author name and surname.
- **Filtering**: Users can filter books genre, authors, publication date and title.

## Setup

1. Clone the repository:
    ```bash
    git clone {my repository}
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run migrations:
    ```bash
    python manage.py migrate
    ```

4. Create a superuser for admin access:
    ```bash
    python manage.py createsuperuser
    ```

5. Run the server:
    ```bash
    python manage.py runserver
    ```

6. Access the admin panel at `http://127.0.0.1:8000/admin/
   
