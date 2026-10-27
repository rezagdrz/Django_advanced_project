from rest_framework import serializers
from ...models import Post ,Category
from accounts.models import Profile
from accounts.models import User , Profile

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']

class PostSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source = 'get_snippet')
    reletavie_url = serializers.URLField(source = 'get_absolute_api_url',read_only =True)
    absolute_url = serializers.SerializerMethodField()
    is_author = serializers.SerializerMethodField()
    author = serializers.ReadOnlyField(source = 'author.user.email')

    class Meta:
        model = Post
        fields = ['id','title','status','content','published_date','image','author','is_author','category','snippet','reletavie_url','absolute_url']

    def get_absolute_url(self,obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)

    def get_is_author(self,obj):
        request = self.context.get('request')
        return request.user.email == obj.author.user.email
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        request = self.context.get('request')
        if request.parser_context.get('kwargs').get('pk'):
            rep.pop('snippet')
            rep.pop('reletavie_url')
            rep.pop('absolute_url')
        else:
            rep.pop('content')
        rep['category']=CategorySerializer(instance.category).data
        return rep
    
    def create(self, validated_data):
        validated_data['author']=Profile.objects.get(user=self.context.get('request').user)
        return super().create(validated_data)

