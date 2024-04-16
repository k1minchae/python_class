from django.shortcuts import render, redirect
from .forms import CreateAuthor, CreateBook
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
User = get_user_model()
from .models import Book, Author
# Create your views here.
def index(request):
    return render(request, 'libraries/index.html')

def books(request):
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'libraries/books.html', context)

def create_author(request):
    user = User.objects.get(pk=request.user.pk)
    if request.method == "POST":
        form = CreateAuthor(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.user = user
            author.save()
            return redirect('accounts:profile', request.user.username)
    form = CreateAuthor()
    context = {
        'form':form
    }
    return render(request, 'libraries/createauthor.html', context)

@login_required
def create_book(request):
    if request.method=='POST':
        form = CreateBook(request.POST)
        if form.is_valid():
            form.save()
            return redirect('libraries:books')
    form = CreateBook()
    context = {
        'form':form,
    }
    return render(request, 'libraries/createbook.html', context)

def author_books(request, author_pk):
    author = Author.objects.get(pk=author_pk)
    books = Book.objects.filter(author=author.pk)
    context = {
        'books':books,
        'author': author,
    }
    return render(request, 'libraries/author_books.html', context)

@login_required
def subscribe(request, author_pk):
    author = Author.objects.get(pk=author_pk)
    if request.user != author.user:
        if author in request.user.subscriptions.all():
            request.user.subscriptions.remove(author)
        else:
            request.user.subscriptions.add(author)
    return redirect('libraries:author_books', author.pk)
