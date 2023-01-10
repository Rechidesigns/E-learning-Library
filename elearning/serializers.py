from rest_framework import serializers
from .models import Category, Book



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description', 'time']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['category', 'title', 'author', 'pages', 'image', 'price', 'website', 'status', 'time']

 