"""Vistas para el inicio de sesión de usuarios."""
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.contrib.auth.forms import AuthenticationForm

class LoginView(generic.FormView):
    form_class = AuthenticationForm
    template_name = 'registration/login.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return redirect(self.success_url)
        return self.form_invalid(form)