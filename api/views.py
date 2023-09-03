# from rest_framework import status
# from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView, Response, Request
from api.serializers import ProductSerializer, CategorySerializer, CommentSerializer, RatingSerializer, RatingCommentSerializer
from product.models import Products, Category
from comment.models import Comment
from rating.models import Rating
# from rest_framework.viewsets import ModelViewSet

# class ProductViewSet(ModelViewSet):
#     queryset = Products.objects.all()
#     serializer_class = ProductSerializer

class CategoryApiView(APIView):
    def get(self, request: Request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)

        return Response(serializer.data)
class ProductApiView(APIView):
    def get(self, request: Request):
        products = Products.objects.all()
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)

    # def post(self, request: Request):
    #     serializer = ProductSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #
    # def put(self, request: Request, pk):
    #     product = get_object_or_404(Products, pk=pk)
    #     serializer = ProductSerializer(product, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def delete(self, request: Request, pk):
    #     product = get_object_or_404(Products, pk=pk)
    #     product.delete()
    #
    #     return Response(status=status.HTTP_204_NO_CONTENT)
class CommentApiView(APIView):
    def get(self, request: Request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)

        return Response(serializer.data)
class RatingApiView(APIView):
    def get(self, request: Request):
        ratings = Rating.objects.all()
        serializer = RatingSerializer(ratings, many=True)

        return Response(serializer.data)
class RatingCommentApiView(APIView):
    def post(self, request: Request):
        serializer_pk = RatingCommentSerializer(data=request.data)
        if serializer_pk.is_valid():
            serializer_data = int(serializer_pk.data.get('pk'))
            ratings = Rating.objects.filter(product=serializer_data)
            serializer1 = RatingSerializer(ratings, many=True)
            comments = Comment.objects.filter(product=serializer_data)
            serializer2 = CommentSerializer(comments, many=True)
        return Response(serializer1.data+serializer2.data)

