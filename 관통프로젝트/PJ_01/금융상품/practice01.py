import requests
import pprint

def get_deposit_products():
    # 본인의 API KEY 로 수정합니다.
    api_key = 'f1ceec09de537229456f8330c7e3b0a8'
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    fin_base = [] # baselist 에서 금융코드만 뽑음
    fin_option = [] # optionlist 에서 금융코드만 뽑음
    common_option = [] # 공통코드중 option 정보 
    common_base = [] # 공통 코드중 base 정보 
    intr_rate = []  # 이 안에 금리정보 dict 저장되어있음.
    final_list = []

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

# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_deposit_products()
    pprint.pprint(result)