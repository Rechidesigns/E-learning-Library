
from django.urls import path, include
from .views import CategoryAPIView
from rest_framework.routers import DefaultRouter
# from .views import BookAPIView

urlpatterns = [
    path('category', CategoryAPIView.as_view()),
    # path('category/book', BookAPIView.as_view()),
    
]
