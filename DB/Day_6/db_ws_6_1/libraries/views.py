from django.shortcuts import render, redirect
from .forms import CreateAuthor

# Create your views here.
def index(request):
    return render(request, 'libraries/index.html')

def books(request):
    return render(request, 'libraries/books.html')

def create_author(request):
    if request.method == "POST":
        form = CreateAuthor(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            return redirect('accounts:profile')
    form = CreateAuthor()
    context = {
        'form':form
    }
    return render(request, 'libraries/createauthor.html', context)