from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, get_user
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, CustomUserUpdateForm, CustomstaffForm


# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('stores:index')
    else:
        form = AuthenticationForm()
    context = {
        'form':form
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('accounts:login')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('stores:index')

    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)

User = get_user_model()
def index(request):
    if request.user.is_staff:
        users = User.objects.all()
        context = {
            'users':users
        }
        return render(request, 'accounts/index.html', context)
    return render(request, 'accounts/ban.html')
def update(request, user_pk):
    user = User.objects.get(pk=user_pk)
    if request.method == 'POST':
        form = CustomUserUpdateForm(request.POST, instance = user)
        if form.is_valid():
            user = form.save(commit=False)

            user.save()
            return redirect('accounts:index')
    else:
        form = CustomUserUpdateForm(instance = user)
    context = {
        'form':form,
    }
    return render(request, 'accounts/update.html', context)

def update_staff(request, user_pk):
    if request.user.is_superuser:
        user = User.objects.get(pk=user_pk)
        if request.method =='POST':
            form = CustomstaffForm(request.POST, instance = user)
            if form.is_valid():
                form.save()
                return redirect('accounts:update_staff', user.pk)
        else:
            form = CustomstaffForm(instance = user)
        context = {
            'user':user,
            'form':form,
        }
        return render(request, 'accounts/staff.html', context)
    return render(request, 'accounts/ban.html')

def delete(request, user_pk):
    if request.user.is_superuser:
        user = User.objects.get(pk=user_pk)
        user.delete()
        return redirect('accounts:index')
    return render(request, 'accounts/ban.html')