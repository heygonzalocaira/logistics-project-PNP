from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse


def login_user(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['uname']
            password = request.POST['psw']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('index'))
            else:
                return render(request, 'vistas/login.html', {'message': "Fallo la autenticación"})
        else:
            return render(request, 'vistas/login.html')
    else:
        return redirect(reverse('index'))


@login_required
def logout_user(request):
    logout(request)
    return redirect('/')


@login_required
def index_tramite(request):
    return render(request, 'vistas/index.html')