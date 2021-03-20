from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from authcustom.forms import *


@csrf_protect
def login_view(request):
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
