from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy

# 💥 SPLIT AUTH IMPORTS
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout

from . import models

# View: List all books
def show_books(request):
    books = models.Book.objects.all()
    return render(request, "list_books.html", {"books": books})

# View: Library detail
class LibraryDetailView(DetailView):
    model = models.Library
    template_name = "library_detail.html"
    context_object_name = "library"

# View: Register user
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

# View: Login user
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('show-books')
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

# View: Logout user
def logout_view(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')