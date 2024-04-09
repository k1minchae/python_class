from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from libraries.models import Author

# Create your views here.
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('index')
    form = AuthenticationForm()
    context = {
        'form':form
    }
    return render(request, 'accounts/login.html', context)

def signup(request):
    if request.method =='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('index')
    form = CustomUserCreationForm()
    context = {
        'form':form
    }
    return render(request, 'accounts/signup.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('index')

User = get_user_model()
@login_required
def signout(request):
    User.delete(request.user)
    auth_logout(request)
    return redirect('index')

def profile(request, username):
    person = User.objects.get(username=username)
    authors = Author.objects.filter(user=person.pk)
    context = {
        'person':person,
        'authors':authors,
    }
    return render(request, 'accounts/profile.html', context)

