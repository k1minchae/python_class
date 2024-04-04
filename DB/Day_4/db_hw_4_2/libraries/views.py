from django.shortcuts import render, redirect
from .models import Book, Review
from accounts.models import User
from .forms import ReviewForm

# Create your views here.
def index(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'libraries/index.html', context)

def detail(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    comments = Review.objects.filter(book=book.pk)
    review_form = ReviewForm()
    context = {
        'review_form':review_form,
        'comments':comments,
        'book':book,
    }
    return render(request, 'libraries/detail.html', context)

def create_comment(request, book_pk):
    book = Book.objects.get(pk = book_pk)
    review_form = ReviewForm(request.POST)
    if review_form.is_valid():
        review = review_form.save(commit=False)
        review.book = book
        review.user = request.user
        review.save()
        return redirect('libraries:detail', book.pk)

def delete_comment(request, book_pk, comment_pk):
    book = Book.objects.get(pk = book_pk)
    review = Review.objects.get(pk = comment_pk)
    review.delete()
    return redirect('libraries:detail', book_pk)