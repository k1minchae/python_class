from django.shortcuts import render, redirect
from .models import Movie, Comment
from .forms import CreateComment, CreateMovie


# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies':movies,
    }
    return render(request, 'movies/index.html', context)

def detail(request, movie_pk):
    movie = Movie.objects.get(pk = movie_pk)
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
                movie = form.save()
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
    if request.user.is_authenticated:
        movie = Movie.objects.get(pk=movie_pk)
        movie.delete()
        return redirect('movies:index')
    return render(request, 'accounts/ban.html')