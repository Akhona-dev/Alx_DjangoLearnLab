from django.urls import path
from . import views

urlpatterns = [
    path('books-available/', views.show_books, name='show-books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library-details'),

    # Custom function-based auth views
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]