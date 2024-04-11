from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import render
from .models import Book
from .serializers import BookListSerializer, BookSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def book_list(request):
    books = Book.objects.all()
    if request.method=='GET':
        serializer = BookListSerializer(books, many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def book_detail(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        data = {
            'delete': f'도서 고유번호 {book.isbn}번의 {book.title}을 삭제했습니다.'
        }
        book.delete()
        
        return Response(data, status=status.HTTP_204_NO_CONTENT)



