from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView
from django.contrib.auth import authenticate
from django.contrib.auth import login  # ALX expects this
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse_lazy

from . import models

# ----------------------------
# Book-related views
# ----------------------------

def show_books(request):
    books = models.Book.objects.all()
    context = {
        "books": books
    }
    return render(request, "list_books.html", context)


class LibraryDetailView(DetailView):
    model = models.Library
    template_name = "library_detail.html"
    context_object_name = "library"

# ----------------------------
# Authentication views
# ----------------------------

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # login must be used
            return redirect('show-books')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'registration/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')
