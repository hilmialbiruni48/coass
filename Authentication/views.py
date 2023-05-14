from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse

from .models import Login
from .forms import LoginForm, CreateUserForm

# Create your views here.

from .models import *

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # request.session['username'] = request.user.username
            return redirect('main:home')
        else:
            messages.info(request, "Username OR password is incorrect")
    return render(request, 'login.html', {})

def logoutUser(request):
    logout(request)
    return redirect('Authentication:login')




def signupPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request, "Account was created for " + user)
            return redirect('Authentication:login')

    response = {'form': form}
    return render(request, 'register.html', response)

@csrf_exempt
def login_with_flutter(request) :
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username = username, password = password)
    print(user)

    if user is not None:
        if user.is_active:
            auth_login(request,user)
            return JsonResponse({"status": True, "username": request.user.username, "message": "Login Berhasil!"}, status=200)
        else:
            return JsonResponse({"status": False, "message": "Gagal login, Akun tidak bisa diakses"}, status=401)
    else :
        return JsonResponse({"status": False, "message": "Gagal login, Username/Password tidak sesuai"}, status=401)

@csrf_exempt
def logout_with_flutter(request):
    try:
        logout(request)
        return JsonResponse({
                "status": True,
                "message": "Successfully Logged out!"
            }, status=200)
    except:
        return JsonResponse({
          "status": False,
          "message": "Failed to Logout"
        }, status=401)

