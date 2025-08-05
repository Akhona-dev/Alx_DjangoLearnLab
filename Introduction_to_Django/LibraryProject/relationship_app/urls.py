from django.urls import path
from . import views, admin_view, librarian_view, member_view
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('books-available/', views.show_books, name='show-books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library-details'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    path('admin/', admin_view.admin_view, name='admin-view'),
    path('librarian/', librarian_view.librarian_view, name='librarian-view'),
    path('member/', member_view.member_view, name='member-view'),
]