from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CategorySerializer, BookSerializer
from elearning.models import Category, Book

class CategoryAPIView(APIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        category = Category.objects.all()
        return category

    def get(self, request, *args, **kwargs):
        category = self.get_queryset()
        serializer = CategorySerializer(category, many = True)

        return Response(serializer.data)