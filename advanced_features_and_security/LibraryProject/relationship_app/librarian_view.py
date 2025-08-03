from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile

@login_required
def librarian_view(request):
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        return redirect('login')

    if profile.role != 'Librarian':
        return redirect('unauthorized')

    return render(request, 'relationship_app/librarian_view.html')