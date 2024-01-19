import pprint
import requests

# 상품과 옵션 정보들을 담고 있는 새로운 객체를 만들어 반환하시오.
# [힌트] 상품 리스트와 옵션 리스트를 금융상품 코드를 기준으로 매칭할 수 있습니다.
# [힌트] 아래와 같은 순서로 데이터를 출력하며 진행합니다.
# 1. 응답을 json 형식으로 변환합니다.
# 2. key 값이 "result" 인 데이터를 변수에 저장합니다.
# 3. 2번의 결과 중 key 값이 "baseList" 인 데이터를 변수에 저장합니다.
# 4. 2번의 결과 중 key 값이 "optionList" 인 데이터를 변수에 저장합니다.
# 5. 3번에서 저장된 변수를 순회하며, 4번에서 저장된 값들에서 금융 상품 코드가 
#     같은 모든 데이터들을 가져와 새로운 딕셔너리로 저장합니다.
#     저장 시, 명세서에 맞게 출력되도록 저장합니다.
# 6. 5번에서 만든 딕셔너리를 결과 리스트에 추가합니다.


def get_deposit_products():
    # 본인의 API KEY 로 수정합니다.
    api_key = 'f1ceec09de537229456f8330c7e3b0a8'
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    fin_base = [] # baselist 에서 금융코드만 뽑음
    fin_option = [] # optionlist 에서 금융코드만 뽑음
    common_option = [] # 공통코드중 option 정보 
    common_base = [] # 공통 코드중 base 정보 
    intr_rate = []  # 이 안에 금리정보 dict 저장되어있음.
    final_list = [] # base 정보를 더한 최종 출력값

    # 요구사항에 맞도록 이곳의 코드를 수정합니다.
    data = requests.get(url).json()
    base_list = data['result']['baseList']
    option_list = data['result']['optionList']

    for i in base_list:
        fin_base.append(i['fin_prdt_cd'])

    for j in option_list:
        fin_option.append(j['fin_prdt_cd'])
        if j['fin_prdt_cd'] in fin_base:
            common_option.append(j)

    for k in base_list:
        if k['fin_prdt_cd'] in fin_option:
            common_base.append(k)

    for l in common_option:
        new_dict_o = {}
        new_dict_o['저축 금리'] = l['intr_rate']
        new_dict_o['저축 기간'] = l['save_trm']
        new_dict_o['저축금리유형'] = l['intr_rate_type']
        new_dict_o['저축금리유형명'] = l['intr_rate_type_nm']
        new_dict_o['최고 우대금리'] = l['intr_rate2']
        intr_rate.append(new_dict_o)
    
    for o in common_base:
        new_dict_b = {}
        new_dict_b['금리정보'] = intr_rate
        new_dict_b['금융상품명'] = o['fin_prdt_nm']
        new_dict_b['금융회사명'] = o['kor_co_nm']
        final_list.append(new_dict_b)

    return final_list
  
  

if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_deposit_products()
    # prrint.prrint(): json 을 보기 좋은 형식으로 출력
    pprint.pprint(result)