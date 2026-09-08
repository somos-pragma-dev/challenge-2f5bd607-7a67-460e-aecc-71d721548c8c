"""Vistas para la gestión de perfiles de usuario."""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def ProfileView(request):
    return render(request, 'profile/profile.html')