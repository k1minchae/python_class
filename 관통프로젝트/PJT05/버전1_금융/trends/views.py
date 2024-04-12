from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
from .models import Keyword, Trend
import requests
from selenium import webdriver
from .forms import KeywordForm
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import matplotlib as mpl


mpl.rcParams['font.family'] = 'Malgun Gothic'  # 예: 'NanumGothic'을 사용 (설치 필요)
mpl.rcParams['axes.unicode_minus'] = False
# Create your views here.
def keyword(request):
    keywords = Keyword.objects.all()
    if request.method == 'POST':
        form = KeywordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trends:keyword')
    form = KeywordForm()
    context = {
        'form':form,
        'keywords':keywords,
    }
    return render(request, 'trends/keyword.html', context)

def delete(request, pk):
    keyword = Keyword.objects.get(pk=pk)
    keyword.delete()
    return redirect('trends:keyword')

def crawling(request):
    keywords = Keyword.objects.all()
    for keyword in keywords:
        url = f"https://www.google.com/search?q={keyword.name}"
        driver = webdriver.Chrome()
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        # 검색 결과 개수는 result-status id를 사용
        result_stats = soup.select_one('#result-stats')
        result = result_stats.text.split()[2][:-1]
        result = result.replace(',', '')
        if Trend.objects.filter(name=keyword.name).exists():
            trend = Trend.objects.get(name=keyword.name)
            trend.result = int(result)
            trend.save()
        else:
            trend = Trend(name=keyword.name, result=int(result))
            trend.save()
    results = Trend.objects.all()
    context = {
        'results':results
    }
    return render(request, 'trends/crawling.html', context)


def histogram(request):
    trends = Trend.objects.all()
    x = []
    y = []
    for trend in trends:
        x.append(trend.name)
        y.append(trend.result)

    plt.bar(x, y)

    plt.title('Technology Trend Analysis')
    plt.xlabel('검색 키워드')
    plt.ylabel('검색 결과')

    buffer = BytesIO()
    plt.savefig(buffer, format = 'png')
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()
    context = {
        'image': f'data:image/png;base64, {img_base64}',
    }
    return render(request, 'trends/histogram.html', context)

def advanced(request):
    keywords = Keyword.objects.all()
    for keyword in keywords:
        url = f"https://www.google.com/search?q={keyword.name}"
        driver = webdriver.Chrome()
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        # 검색 결과 개수는 result-status id를 사용
        result_stats = soup.select_one('#result-stats')
        result = result_stats.text.split()[2][:-1]
        result = result.replace(',', '')
        if Trend.objects.filter(name=keyword.name, search_period='year').exists():
            trend = Trend.objects.get(name=keyword.name, search_period='year')
            trend.result = int(result)
            trend.save()
        else:
            trend = Trend(name=keyword.name, result=int(result), search_period='year')
            trend.save()
    trends = Trend.objects.filter(search_period='year')
    x = []
    y = []
    for trend in trends:
        x.append(trend.name)
        y.append(trend.result)

    plt.bar(x, y)

    plt.title('Technology Trend Analysis')
    plt.xlabel('검색 키워드')
    plt.ylabel('검색 결과')

    buffer = BytesIO()
    plt.savefig(buffer, format = 'png')
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()
    context = {
        'image': f'data:image/png;base64, {img_base64}',
    }
    return render(request, 'trends/advanced.html', context)