# open 및 json 모듈 사용예시

import json
import os
# 스크립트 파일의 디렉토리 경로 가져오기
script_directory = os.path.dirname(os.path.realpath(__file__))

# 현재 작업 디렉토리를 스크립트 파일의 디렉토리로 변경
os.chdir(script_directory)



book = open('sample.json', encoding='utf-8')
book_detail = json.load(book)

print(book_detail)
