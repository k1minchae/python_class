from django.shortcuts import render
import numpy as np
import pandas as pd
from django.http import JsonResponse
from rest_framework.decorators import api_view
from heapq import heappop, heappush


# CSV 데이터를 DataFrame 으로 변환하여 반환하는 함수
@api_view(['GET'])
def dataframe(request):
    df = pd.read_csv('data/test_data.CSV', encoding='cp949')
    # df.head()
    # records : 리스트 원소를 각각 하나의 레코드를 만들어주는 옵션
    data = df.to_dict('records') 
    return JsonResponse({'data': data})

# 결측 데이터를 처리하는 함수
@api_view(['GET'])
def missing_data(request):
    # df = pd.read_csv('data/test_data_has_null.CSV', encoding='cp949')
    # NaN data 는 True 로 표현됨
    # df.head().isna()

    # 결측치를 빈 문자열로 채운다
    df.fillna('NULL', inplace=True)
    data = df.to_dict('records')

    return JsonResponse({'결측치 처리 데이터': data})

# 평균 나이와 가장 비슷한 10명을 반환하는 함수
df = pd.read_csv('data/test_data_has_null.CSV', encoding='cp949')
def average_age(request):
    average = df['나이'].mean()
    # 벡터화된 연산으로 평균과의 차이 계산
    df['age_difference'] = (df['나이'] - average).abs()
    closest_entries = df.nsmallest(10, 'age_difference').to_dict('records')
    return JsonResponse({'평균 근사값 10명': closest_entries})

# heap 자료구조를 사용하여 직접 알고리즘 구현
# def average_age(request):   
#     average = df['나이'].mean()
#     dfa = df.fillna("NULL")
#     data = dfa.to_dict('records')
#     q = []
#     arr = []
#     for i in range(len(data)):
#         if data[i]['나이'] != "NULL":
#             heappush(q, (abs(data[i]['나이'] - average), i))
#     for i in range(10):
#         arr.append(data[heappop(q)[1]])
#     return JsonResponse({'data': arr})