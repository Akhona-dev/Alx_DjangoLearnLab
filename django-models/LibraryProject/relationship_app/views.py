from django.shortcuts import render , redirect
from django.views.generic import DetailView
from . import models
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your views here.

#first view
#a function that lists all available books and renders a simple text
def show_books(request):
    books = models.Book.objects.all()

    context = {
        "books": books
    }

    return render(request, "list_books.html", context)
    
    ...

#second view
#A class based view
class LibraryDetailView(DetailView):
    model = models.Library
    template_name = "library_detail.html"
    context_object_name = "library"

    ...

#Authentication
#Registration

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

    ...

#logging in

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

    return render(request, 'registration/login.html')

    ...

#logging out

def logout_view(request):
    logout(request)  # Logs the user out by clearing session
    return redirect('login')
