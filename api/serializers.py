from rest_framework import serializers

from product.models import Products, Category
from rating.models import Rating
from comment.models import Comment

class RatingCommentSerializer(serializers.Serializer):
    pk = serializers.IntegerField(max_value=100)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name',]
class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Products
        fields = ['name', 'category']
class RatingSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = Rating
        fields = ['value', 'product']
class CommentSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = Comment
        fields = ['content', 'product']