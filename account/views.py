from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm
from django.contrib.auth.hashers import PBKDF2PasswordHasher
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.conf import settings
from rest_framework_simplejwt import views as jwt_views
import json
import requests

# Create your views here.
# View to Login 
def login_view(request, *args, **kwargs):
    user = request.user
    context = {}
    form = LoginForm(request.POST or None)
    if user.is_authenticated:
        return HttpResponse('You are already authenticated')
    if form.is_valid():
        if user is not None:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        context['login_form'] = form
    return render(request, 'login.html', context)

