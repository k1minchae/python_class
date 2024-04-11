from rest_framework import serializers
from .models import Book

class BookListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title',)

class BookDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'