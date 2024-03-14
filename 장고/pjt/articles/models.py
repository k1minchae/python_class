from django.db import models

# Create your models here.
# CRUD : Create, Read, Update(수정), Delete

class Article(models.Model):
    title = models.CharField(max_length = 20)
    content = models.TextField()
    # 초기 저장에만 시간 저장
    create_at = models.DateTimeField(auto_now_add=True)
    # 세이브 될때마다 갱신되는 시간
    update_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        # 앞에 고유번호가 있던 게시물이 삭제되어도 다음 게시물이 그 번호를 채우지 않는다.
        return f'[{self.pk}번 게시물: {self.title}]'
    