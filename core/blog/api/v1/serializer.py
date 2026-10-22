from rest_framework import serializers
from ...models import Post ,Category
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','title','status','content','published_date','image','author','category']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']