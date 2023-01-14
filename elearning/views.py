from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CategorySerializer, BookSerializer
from elearning.models import Category, Book
from rest_framework import status
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework_simplejwt.authentication import JWTAuthentication
from account.permissions import IsAdminOrReadOnly


class CategoryCreateView(APIView):
    """
    This method creates a category of books 
    """
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
    """
    this method is used to view all category of books
    """
    serializer_class = CategorySerializer

    def get_queryset(self):
        category = Category.objects.all()
        return category

    def get(self, request, *args, **kwargs):
        category = self.get_queryset()
        serializer = CategorySerializer(category, many=True)

        return Response(serializer.data)


class CategoryDeleteAPIView(APIView):
    """
    this method is used to delete a category
    """
    serializer_class = CategorySerializer
    
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAdminOrReadOnly]

    queryset = Category.objects.all()

    def update(self, request, *args, **kwargs) :
        super().update(request, *args, **kwargs)
        return Response({'success': 'updated successful.'}, status=200)

    def destroy(self, request, *args, **kwargs) :
        super().destroy(request, *args, **kwargs)
        return Response({'success': 'deleted successful.'}, status=200)



class BookCreateAPIView(APIView):
    """
    this method is used to create books
    """

    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAdminOrReadOnly]

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
    """
    this method is used to view all books
    """
    serializer_class = BookSerializer

    def get_queryset(self):
        book = Book.objects.all()
        return book

    def get(self, request):
        book = self.get_queryset()
        serializer = BookSerializer(book, many=True)

        return Response(serializer.data)



class BookDeleteAPIView(APIView):
    """
    this method is used to delete a book
    """
    serializer_class = BookSerializer
    
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAdminOrReadOnly]

    queryset = Book.objects.all()

    def update(self, request, *args, **kwargs) :
        super().update(request, *args, **kwargs)
        return Response({'success': 'updated successful.'}, status=200)

    def destroy(self, request, *args, **kwargs) :
        super().destroy(request, *args, **kwargs)
        return Response({'success': 'deleted successful.'}, status=200)

