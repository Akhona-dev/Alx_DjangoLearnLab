from django.urls import path
from . import views

urlpatterns = [
    path('books-available/', views.show_books, name='show-books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library-details'),
    path('signup/',views.SignUpView.as_view(), name = 'signup'),
    path('login/',views.login_view, name = 'login'),
    path('logout/',views.logout_view, name = 'logout'),
]