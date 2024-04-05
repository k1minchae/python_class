from django.shortcuts import render
import matplotlib.pyplot as plt

# 파이썬에서 입출력 연산을 위한 표준 라이브러리
# BytesIO : 이진데이터를 다루기 위한 버퍼를 제공
from io import BytesIO

# 텍스트 <-> 이진 데이터를 변환하는 모듈
import base64 


# CSV 파일 읽어오는법 : pandas , numpy
import pandas as pd
CSV_path = 'austin_weather.CSV'


# Create your views here.
def index(request):
    x = [1, 2, 3, 4]
    y = [2, 4, 6, 8]

    plt.plot(x, y)
    plt.title('test graph')
    plt.xlabel('xlabel')
    plt.ylabel('ylabel')

    # 새 창이 열려버림
    # plt.show()


    # 비어있는 버퍼 생성 -> io모듈로
    buffer = BytesIO()

    # 버퍼에 그래프를 저장하는 코드(png형태)
    plt.savefig(buffer, format = 'png')

    # 버퍼의 내용을 인코딩을 해서 써야함 (임시공간이라서 저장은안됨)
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()

    # CSV 파일 읽어오기
    df = pd.read_csv(CSV_path)
    
    context = {
        'image': f'data:image/png;base64, {img_base64}',
        'df':df,
    }

    return render(request, 'myapps/index.html', context)


