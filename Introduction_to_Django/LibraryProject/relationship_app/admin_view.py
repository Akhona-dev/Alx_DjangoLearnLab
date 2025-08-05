from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import UserProfile

@login_required
def admin_view(request):
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        return redirect('login') 

    if profile.role != 'Admin':
        return redirect('unauthorized') 

    return render(request, 'relationship_app/admin_view.html')