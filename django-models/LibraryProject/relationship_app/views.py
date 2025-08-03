from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib import messages

from . import models

# View to list all available books
def show_books(request):
    books = models.Book.objects.all()
    return render(request, "list_books.html", {"books": books})

# Detail view for a library
class LibraryDetailView(DetailView):
    model = models.Library
    template_name = "library_detail.html"
    context_object_name = "library"

# Register a new user
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Logs in the user after registration
            return redirect('show-books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Log a user in
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('show-books')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'relationship_app/login.html')

# Log a user out
def logout_view(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')