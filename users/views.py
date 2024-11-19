from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import auth

@login_required
def logout(request):
    auth.logout(request)
    return render(request, 'users/logout.html')