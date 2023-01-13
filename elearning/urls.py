
from django.urls import path, include
from .views import CategoryAPIView, CategoryCreateView, CategoryDeleteAPIView
from rest_framework.routers import DefaultRouter
from .views import BookCreateAPIView, BookViewApi,BookDeleteAPIView

urlpatterns = [
    path('category/', CategoryAPIView.as_view()),
    path('category/create', CategoryCreateView.as_view()),
    path('category/delete/<int:pk>/', CategoryDeleteAPIView.as_view(), name='category-delete'),
    path('category/book', BookCreateAPIView.as_view()),
    path('category/bookview', BookViewApi.as_view()),
    path('category/book/delete/<int:pk>/', BookDeleteAPIView.as_view(), name='book-delete'),
]
