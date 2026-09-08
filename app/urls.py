"""Configuración de URLs del proyecto Django."""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', include('app.views.registration')),
    path('login/', include('app.views.login')),
    path('profile/', include('app.views.profile')),
]