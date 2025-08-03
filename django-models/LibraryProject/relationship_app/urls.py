from django.urls import path
from . import views
from django.contrib.auth.views import LoginView ,LogoutView

urlpatterns = [
    path('books-available/', views.show_books, name='show-books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library-details'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]