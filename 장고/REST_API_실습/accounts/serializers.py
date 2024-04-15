from rest_framework import serializers
from django.contrib.auth import get_user_model
from articles.models import Article

# form 쓸 때랑 똑같다
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields= ('username', 'password', 'nickname',)

    # 비밀번호가 그대로 저장되므로 암호화 필요 -> 재정의
    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user

class UserArticleListSerializer(serializers.ModelSerializer):
    # 역참조를 이용해서 유저가 작성한 article list 추가
    # 1. article 은 title, content 등 데이터가 여러개
    # => nested_serializer를 정의
    class ArticleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = '__all__'

    # article_set 을 내맘대로 이름 바꾸면 안 됨 -> 항상 모델이 아는 필드명으로 작성
    article_set = ArticleSerializer(many=True)

    class Meta:
        model = get_user_model()
        # 필드에 article_set 필드 추가
        fields = ('nickname', 'username', 'article_set',)