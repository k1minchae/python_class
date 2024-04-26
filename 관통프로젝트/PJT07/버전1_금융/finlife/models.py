from django.db import models

# Create your models here.
class DepositProducts(models.Model):
    join_deny_choices = [
        (1 , '제한없음'),
        (2 , '서민전용'),
        (3 , '일부 제한'),
    ]
    fin_prdt_cd = models.TextField()    # 금융상품 코드
    kor_co_no = models.TextField()      # 금융회사명
    fin_prdt_nm = models.TextField(unique=True)    # 금융 상품명
    etc_note = models.TextField()       # 금융 상품 설명
    join_deny = models.IntegerField(choices=join_deny_choices) # 가입 제한
    join_member = models.TextField()    # 가입 대상
    join_way = models.TextField()       # 가입 방법
    spcl_cnd = models.TextField()       # 우대 조건

class DepositOptions(models.Model):
    product = models.ForeignKey(DepositProducts, on_delete = models.CASCADE) # 외래키
    fin_prdt_cd = models.TextField()    # 금융상품 코드
    intr_rate_type_nm = models.CharField(max_length=100) # 저축 금리 유형명
    intr_rate = models.FloatField(default=-1)     # 저축 금리
    intr_rate2 = models.FloatField(default=-1)    # 최고 우대금리
    save_trm = models.IntegerField()    # 저축 기간