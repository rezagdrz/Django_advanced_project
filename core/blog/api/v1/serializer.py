from rest_framework import serializers
from ...models import Post
class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.first_name')
    class Meta:
        model = Post
        fields = ['title','status','author','content']