from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .serializers import CategorySerializer, BookSerializer
from rest_framework import viewsets
from .models import Category, Book

# Create your views here.

class CategoryView(viewsets.ModelViewSet):
            queryset = Category.objects.all()
            serializer_class = CategorySerializer




class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
