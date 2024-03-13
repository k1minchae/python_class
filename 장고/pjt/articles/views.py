from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'name' : 'Jane'
    }
    # render 함수의 3번째 항목에는 매개변수(딕셔너리)가 들어감
    return render(request, 'articles/index.html', context)

import random
def dinner(request):
    foods = ['쭈꾸미', '떡볶이', '초밥', '치킨', '피자']
    picked = random.choice(foods)
    context = {
        'foods' : foods,
        'picked' : picked,
    }
    return render(request, 'articles/dinner.html', context)

def search(request):
    return render(request, 'articles/search.html')

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    message = request.GET.get('query')
    context = {
        'message': message
    }
    return render(request, 'articles/catch.html', context)

def detail(request, num):
    context = {
        'num':num,
    }
    # articles/articles/1 --> 1이라는 값이 num 에 전달되어 함수 안에서 사용
    return render(request, 'articles/detail.html', context)
