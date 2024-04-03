from django.shortcuts import render, redirect
from .models import Author, Book
from .forms import BookForm

# Create your views here.
def index(request):
    authors = Author.objects.all()
    context = {
        'authors': authors,
        
    }
    
    return render(request, 'libraries/index.html', context)

def detail(request, author_pk):
    author = Author.objects.get(pk=author_pk)
    form = BookForm()
    books = author.book_set.all()
    context = {
        'books': books,
        'author': author,
        'form': form,
    }
    return render(request, 'libraries/detail.html', context)

def create(request, author_pk):
    author = Author.objects.get(pk=author_pk)
    form = BookForm(request.POST)
    if form.is_valid():
        book = form.save(commit = False)
        book.author = author # 외래키 데이터 입력
        book.save()
        return redirect('libraries:detail', author.pk)
    context = {
        'author': author,
        'form': form,
    }
    return render(request, 'libraries/detail.html', context)