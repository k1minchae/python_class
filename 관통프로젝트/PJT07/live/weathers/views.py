from django.shortcuts import render
from django.http import JsonResponse
import requests
from django.conf import settings
from .serializers import WeatherSerializer
from .models import Weather
from rest_framework.response import Response
from rest_framework.decorators import api_view

API_KEY = settings.WEATHER_API_KEY
cityname = 'Seoul,KR'
url = f'http://api.openweathermap.org/data/2.5/forecast?q={cityname}&appid={API_KEY}'

# Create your views here.
def index(request):    
    response = requests.get(url).json()
    return JsonResponse(response)

# 원하는 데이터만 DB에 저장

def save_data(request):
    response = requests.get(url).json()
    for li in response.get('list'):
        dt_txt = li.get('dt_txt')
        temp = li.get('main').get('temp')
        feels_like = li.get('main').get('feels_like')
        
        # 저장할수 있도록 변환 -> serializer -> is_valid확인
        save_data = {
            'dt_txt':dt_txt,
            'temp':temp,
            'feels_like':feels_like,
        }
        # 변환
        serializer = WeatherSerializer(data=save_data)

        # 유효성 검증 -> 버그날때 해당 버그 리턴
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse({'message': '저장완료'})
@api_view(['GET'])
def list_data(request):
    weathers = Weather.objects.all()
    serializers = WeatherSerializer(weathers, many=True)
    
    return Response(serializers.data)

@api_view(['GET'])
def hot_weathers(request):
    # 단순한 방법
    # # 1. 전체를 가져온다
    # weathers = Weather.objects.all()
    # # 2. 새로운 리스트에다가 조건에 맞는 데이터만 추가
    # hot_weathers = []
    # for weather in weathers:
    #     # 섭씨 온도가 30도가 넘으면 추가
    #     celsius = round(weather.temp - 273.15, 2)
    #     if celsius > 10:
    #         hot_weathers.append(weather)
    # # 3. 포장해서 반환한다.
    # serializers = WeatherSerializer(hot_weathers, many=True) # 리스트도 포장에 넣을수있음
    # return Response(serializers.data)

    # 권장방법
    # __gt : 이상
    weathers = Weather.objects.filter(temp__gt=(19+273.15))
    serialzers = WeatherSerializer(weathers, many=True)
    return Response(serialzers.data)