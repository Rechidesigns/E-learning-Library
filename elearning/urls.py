from django.urls import path, include
from .views import CategoryView, BooksView
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'list', CategoryView)
router.register(r'tile', BooksView)

urlpatterns = [
    path('/', include(router.urls))
]

