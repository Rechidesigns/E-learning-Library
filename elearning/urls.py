from django.urls import path, include
from .views import CategoryView, BookView
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'category', CategoryView)
router.register(r'book', BookView)

urlpatterns = [
    path('/', include(router.urls))
]

