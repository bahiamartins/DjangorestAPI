from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from authcustom.forms import LoginForm


@csrf_protect
def login_view(request):
    form = LoginForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username=email, password=password)
            if user:
                if user.is_active:
                    login(request, user)
            else:
                msg_error = 'Usuário e senha não conferem.'
                messages.error(request, msg_error)

    return render(request, 'authcustom/login.html', {'form': form})
