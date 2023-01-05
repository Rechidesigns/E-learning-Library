from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .serializers import CategorySerializer, BooksSerializer
from rest_framework import viewsets
from .models import Category, Books

# Create your views here.

class CategoryView(viewsets.ModelViewSet):
            queryset = Category.objects.all()
            serializer_class = CategorySerializer




class BooksView(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
