# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login

from authcustom.forms import *

# Create your views here.
@csrf_protect
def login_view(request):
    
    print(request.META['HTTP_HOST'])
    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            user = authenticate(username=email, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)

    else:
        form = LoginForm()
    
    return render(request, 'authcustom/login.html', {'form': form})
