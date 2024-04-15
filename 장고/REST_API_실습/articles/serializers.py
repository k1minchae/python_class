from rest_framework import serializers
from .models import Article
from django.contrib.auth import get_user_model

User = get_user_model()
class ArticleListSerializer(serializers.ModelSerializer):
    # 여기서 user필드의 출력 내용을 바꾸고싶을 때는? -> 재정의
    # source 어떤 내용을 출력할 것인지 설정 : nickname 만 가져오고싶을때
    # user = serializers.CharField(source='user.nickname')
    
    
    # 유저 전체 정보를 가져오고 싶을 때
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = '__all__'

    user = UserSerializer()
    
    class Meta:
        model = Article
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'content',)