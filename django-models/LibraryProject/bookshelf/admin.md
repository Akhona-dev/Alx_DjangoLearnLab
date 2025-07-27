# Admin Setup for Book Model

## File: bookshelf/admin.py

- Book model registered using Django admin.
- list_display includes: title, author, publication_year.
- search_fields configured for title and author.
- list_filter added for publication_year.

Admin interface now supports:
- Viewing books in tabular format.
- Searching by title and author.
- Filtering by year of publication.