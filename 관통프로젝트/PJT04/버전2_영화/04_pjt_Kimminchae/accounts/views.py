from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserUpdateForm
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

User = get_user_model()
# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('movies:index')
    form = AuthenticationForm()
    context = {
        'form':form
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('movies:index')

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('movies:index')
    form = CustomUserCreationForm()
    context = {
        'form':form
    }
    return render(request, 'accounts/signup.html', context)

def signout(request, user_pk):
    user = User.objects.get(pk=user_pk)
    if request.user == user:
        user.delete()
        return redirect('movies:index')
    return render(request, 'accounts/ban.html')

def update(request, user_pk):
    user = User.objects.get(pk=user_pk)
    if request.method == 'POST':
        form = CustomUserUpdateForm(request.POST, instance = user)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    form = CustomUserUpdateForm(instance = user)
    context = {
        'form':form
    }
    return render(request, 'accounts/update.html', context)

def password_change(request, user_pk):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form':form
    }
    return render(request, 'accounts/change_password.html', context)