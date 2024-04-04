from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm


# Create your views here.
def index(request):
    print(request.user.is_authenticated)
    todo_list = Todo.objects.all()
    context = {
        'todo_list': todo_list
    }
    return render(request, 'todos/index.html', context)

def create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = TodoForm(request.POST)
            if form.is_valid():
                todo = form.save(commit=False)
                todo.user = request.user
                todo.save()
                return redirect('todos:detail', todo.pk)
        else:
            form = TodoForm()
        context = {
            'form': form
        }
        return render(request, 'todos/create.html', context)
    return redirect('accounts:login')

def detail(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    context = {
        'todo': todo
    }
    return render(request, 'todos/detail.html', context)


def delete(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    if request.method == 'POST' and request.user == todo.user:
        todo.delete()
        return redirect('todos:index')
    else:
        return redirect('todos:detail', todo.pk)

def update(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    if request.method == 'POST':
        if request.user == todo.user:
            return render(request, 'todos/update.html', context)
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save()
            return redirect('todos:detail', todo.pk)
    else:
        form = TodoForm(instance=todo)
    context = {
        'todo': todo,
        'form': form
    }
    return render(request, 'todos/update.html', context)

def mypage(request):
    if request.method == 'POST':
        pass
    todos = Todo.objects.filter(user = request.user.pk)
    context = {
        'todos':todos
    }
    return render(request, 'todos/my_page.html', context)

