from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CategorySerializer, BookSerializer
from elearning.models import Category, Book

class CategoryCreateView(APIView):
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        data = {}
        serializer.is_valid(raise_exception=True)
        category = serializer.save()
        data['Response'] = 'successfuly added category'
        data["name"] = category.name
        data["description"] = category.description

        return Response(data)


class CategoryAPIView(APIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        category = Category.objects.all()
        return category

    def get(self, request, *args, **kwargs):
        category = self.get_queryset()
        serializer = CategorySerializer(category, many=True)

        return Response(serializer.data)


# class CategoryDeleteAPIView(APIView):
#     def delete(self, request):
#         category = self.object.id



class BookCreateAPIView(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        data = {}
        serializer.is_valid(raise_exception=True)
        Book = serializer.save()
        data['Response'] = 'successfuly added a book'
        data['title'] = Book.title
        data['author'] = Book.author
        data['category'] = Book.category

        return Response(data)

class BookViewApi(APIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        book = Book.objects.all()
        return book

    def get(self, request):
        book = self.get_queryset()
        serializer = BookSerializer(book, many=True)

        return Response(serializer.data)