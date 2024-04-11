from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ArtistSerializers
from .models import Artist

# Create your views here.
@api_view(['POST', 'GET'])
def create(request):
    artist = Artist.objects.all()
    if request.method == 'GET':
        serializer = ArtistSerializers(artist, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = ArtistSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    