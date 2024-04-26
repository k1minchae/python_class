from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
import requests
from rest_framework.response import Response
from .serializers import DepositOptionsSerializer, DepositProductsSerializer
from rest_framework.decorators import api_view
from .models import DepositOptions, DepositProducts
from django.db.models import Max

API_KEY = settings.FIN_API_KEY
url = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'

# Create your views here.
@api_view(['GET'])
def save_deposit_products(request):
    # json 데이터 불러오기
    params = {
        'auth':API_KEY,
        'topFinGrpNo':'020000',
        'pageNo': '1',
    }
    response = requests.get(url, params=params).json()
    # return JsonResponse(response)
    for lists in response['result']['baseList']:
        # 예금 상품 저장
        save_datas = {
            'fin_prdt_cd':lists['fin_prdt_cd'],
            'kor_co_no':lists['fin_co_no'],
            'fin_prdt_nm':lists['fin_prdt_nm'],
            'etc_note':lists['etc_note'],
            'join_deny':lists['join_deny'],
            'join_member':lists['join_member'],
            'join_way':lists['join_way'],
            'spcl_cnd':lists['spcl_cnd']
        }
        product_serializers = DepositProductsSerializer(data=save_datas)
        if product_serializers.is_valid(raise_exception=True):    
            product_serializers.save()
    for lists in response['result']['optionList']:
        fin_prdt_cd = lists['fin_prdt_cd']
        depositproducts = DepositProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
        if depositproducts:
            save_datas = {
                'product':depositproducts.pk,
                'fin_prdt_cd': lists['fin_prdt_cd'],
                'intr_rate_type_nm':lists['intr_rate_type_nm'],
                'intr_rate':lists['intr_rate'],
                'intr_rate2':lists['intr_rate2'],
                'save_trm':lists['save_trm']
            }
            option_serializers = DepositOptionsSerializer(data=save_datas)
            if option_serializers.is_valid(raise_exception=True):
                option_serializers.save(product=depositproducts)
    return JsonResponse({'result':'OK'})

@api_view(['GET', 'POST'])
def deposit_products(request):
    if request.method == 'GET':
        products = DepositProducts.objects.all()
        serializers = DepositProductsSerializer(products, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializer = DepositProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return JsonResponse({'message':'이미 있는 데이터거나 잘못 입력되었습니다.'})

@api_view(['GET'])
def deposit_options(request, fin_prdt_cd):
    option = DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
    if option:
        serializer = DepositOptionsSerializer(option, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def top_rate(request):
    # 최고 이율 찾기
    options = DepositOptions.objects.all()
    option = 0
    product = 0
    rate = 0
    for o in options:
        if o.intr_rate2 > rate:
            rate = o.intr_rate2
            product = o.product
            option = o
    serializer_option = DepositOptionsSerializer(option)
    serializer_product = DepositProductsSerializer(product)

    result = {
        'deposit_product': serializer_product.data,
        'options': serializer_option.data
    }
    return JsonResponse(result)