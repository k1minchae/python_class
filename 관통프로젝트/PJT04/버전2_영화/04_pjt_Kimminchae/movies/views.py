from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Comment
from .forms import CreateComment, CreateMovie
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies':movies,
    }
    return render(request, 'movies/index.html', context)

def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    form = CreateComment()
    comments = Comment.objects.filter(movie = movie.pk)
    context = {
        'comments':comments,
        'form':form,
        'movie':movie,
    }
    return render(request, 'movies/detail.html', context)

def create(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = CreateMovie(request.POST, request.FILES)
            if form.is_valid():
                movie = form.save(commit=False)
                movie.user = request.user
                movie.save()
                return redirect('movies:detail', movie.pk)
        form = CreateMovie()
        context = {
            'form':form,
        }
        return render(request, 'movies/create.html', context)
    return render(request, 'accounts/ban.html')

def update(request, movie_pk):
    if request.user.is_authenticated:
        movie = Movie.objects.get(pk=movie_pk)
        if request.method == 'POST':
            form = CreateMovie(request.POST, request.FILES, instance=movie)
            if form.is_valid():
                form.save()
                return redirect('movies:detail', movie.pk)
        form = CreateMovie(instance=movie)
        context = {
            'form':form,
        }
        return render(request, 'movies/update.html', context)
    return render(request, 'accounts/ban.html')

def create_comment(request, movie_pk):
    if request.user.is_authenticated:
        movie = Movie.objects.get(pk=movie_pk)
        form = CreateComment(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.movie = movie
            comment.save()
        return redirect('movies:detail', movie.pk)
    return render(request, 'accounts/ban.html')
    
def delete(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.user.is_authenticated and movie.user == request.user:
        movie.delete()
        return redirect('movies:index')
    return render(request, 'accounts/ban.html')

def delete_comment(request, movie_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user.is_authenticated and comment.user == request.user:
        comment = Comment.objects.get(pk=comment_pk)
        comment.delete()
        return redirect('movies:detail', movie_pk)
    else:
        return render(request, 'accounts/ban.html')
    
def like(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if movie.user != request.user:
        if request.user in movie.like_users.all():
            movie.like_users.remove(request.user)
        else:
            movie.like_users.add(request.user)
        return redirect('movies:detail', movie.pk)
    else:
        return render(request, 'accounts/ban.html')