from rest_framework import generics
from django_filters import rest_framework as filters
from blog.models import Post

class PostFilter(filters.FilterSet):

    from_time=filters.DateTimeFilter(field_name="published_date", lookup_expr='gte')
    to_time = filters.DateTimeFilter(field_name="published_date", lookup_expr='lte')
    class Meta:
        model = Post
        fields = ['category', 'author']
        