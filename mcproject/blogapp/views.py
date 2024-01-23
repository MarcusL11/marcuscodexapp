from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Subscriber
from .forms import CreateUserForm, UserLoginForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request, 'blogapp/index.html')

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                form.cleaned_data['username'],
                form.cleaned_data['email'],
                form.cleaned_data['password1']
            )
            subscriber = Subscriber.objects.create(
                user=user,
            )
            subscriber.save()
            return redirect("login")
        else:
            return render(request, 'blogapp/register.html', {'form': form})

    return render(request, 'blogapp/register.html', {'form': form})

def user_login(request):
    form = UserLoginForm()

    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("profile")
            else:
                form.add_error(None, "Invalid username or password")

    return render(request, 'blogapp/login.html', {'form': form})

def user_logout(request):  
    logout(request)  
    return redirect("home")

@login_required(login_url="login")
def profile(request):
    return render(request, 'blogapp/profile.html')
