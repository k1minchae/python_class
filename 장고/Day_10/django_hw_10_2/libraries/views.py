from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import BookListSerializers, BookDetailSerializers
from .models import Book

# Create your views here.

@api_view(['GET'])
def book_list(request):
    book = Book.objects.all()
    if request.method == 'GET':
        serializer = BookListSerializers(book, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def book_detail(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    if request.method == 'GET':
        serializer = BookDetailSerializers(book)
        return Response(serializer.data)