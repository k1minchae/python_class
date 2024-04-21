from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods


User = get_user_model()
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('boards:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("boards:index")
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)




def logout(request):
    auth_logout(request)
    return redirect('boards:index')

def profile(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    followers = user.followers.all()
    boards = user.board_set.all()
    comments = user.comment_set.all()
    followings = get_user_model().objects.filter(followers=user.pk)
    context = {
        'followings': followings,
        'comments':comments,
        'boards': boards,
        'followers':followers,
        'user':user
    }
    return render(request, 'accounts/profile.html', context)

@login_required
@require_http_methods(['POST', 'GET'])
def follow(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    if request.user != user.pk:
        if request.user in user.followers.all():
            user.followers.remove(request.user)
        else:
            user.followers.add(request.user)
        return redirect('accounts:profile' ,user.pk)
