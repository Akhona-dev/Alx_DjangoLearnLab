from django.shortcuts import render
from django.views.generic import DetailView
from . import models
# Create your views here.

#first view
#a function that lists all available books and renders a simple text
def show_books(request):
    books = models.Book.objects.all()

    context = {
        "books": books
    }

    return render(request, "list_books.html", context)

#second view
#A class based view
class LibraryDetailView(DetailView):
    model = models.Library
    template_name = "library_detail.html"
    context_object_name = "library"

#Authentication
#Registration
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'