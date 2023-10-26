from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

class Sign_Up(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'sign_up.html'
    success_url = reverse_lazy('login')

def success(request):
    return render(request,'success.html')

class Login(LoginView):
    template_name = 'login.html'
    next_page = 'success'

class Log_out(LogoutView):
    next_page = '/'