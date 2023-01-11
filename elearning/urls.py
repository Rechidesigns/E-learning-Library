
from django.urls import path, include
from .views import CategoryAPIView, CategoryCreateView
from rest_framework.routers import DefaultRouter
from .views import BookCreateAPIView, BookViewApi

urlpatterns = [
    path('category/', CategoryAPIView.as_view()),
    path('category/create', CategoryCreateView.as_view()),
    path('category/book', BookCreateAPIView.as_view()),
    path('category/bookview', BookViewApi.as_view()),
    
]
