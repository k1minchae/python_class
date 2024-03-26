from django.shortcuts import render, redirect
from .models import App

# Create your views here.
def index(request):
    article = App.objects.all()
    context = {
        'articles' : article
    }
    return render(request, 'apps/index.html', context)

def detail(request, pk):
    article = App.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'apps/detail.html', context)

# 페이지 렌더링하는게 끝
def new(request):
    return render(request, 'apps/new.html')

def create(request):
    # 데이터를 포스트 요청을 통해 서버로 전송 -> 보안상 안전
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 코드의 간결성 : 객체를 생성하면서 동시에 속성 설정
    article = App(title = title, content = content)
    # 데이터 관리의 원칙 : 안정성 -> 유효성 검사
    article.save()
    
    return redirect('apps:detail', article.pk)
    # 데이터 변경되었을 때 경로에 요청

def delete(request, pk):
    article = App.objects.get(pk=pk)
    article.delete()

    return redirect('apps:index')

def edit(request, pk):
    article = App.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'apps/edit.html', context)

def update(request, pk):
    article = App.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')    
    
    article.save()

    return redirect('apps:detail', article.pk)
