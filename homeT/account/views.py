from django.shortcuts import render,redirect
from .forms import SigninForm
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.http import HttpResponse

# Create your views here.
def loginpage(request):
    signin_form = SigninForm()
    return render(request, 'account/login.html', {'signin_form': signin_form})

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('mainpage:main')
        else:
            return HttpResponse("다시 시도해보세요!")
    else:
        signin_form = SigninForm()
        return render(request, 'account/login.html', {'signin_form': signin_form})

def signup(request):
    User = get_user_model()
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            return redirect('mainpage:main')
    else:
        return render(request, 'account/signup.html')

