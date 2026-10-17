
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializer import PostSerializer
from ...models import Post
from django.shortcuts import get_object_or_404

@api_view()
def postList(request):
    post = Post.objects.filter(status=True)
    post = PostSerializer(post,many=True)
    return Response(post.data)

@api_view()
def postDetail(request,id):
    post = get_object_or_404(Post,pk=id)
    post = PostSerializer(post)
    return Response(post.data)

#another way to show doesnot exist Post
'''
@api_view()
def postDetail(request,id):
    try:
        post = Post.objects.get(pk=id)
        post = PostSerializer(post)
        return Response(post.data)
    
    except Post.DoesNotExist:
        return Response({'datail':'this post does not exist'},status=status.HTTP_404_NOT_FOUND)
'''
