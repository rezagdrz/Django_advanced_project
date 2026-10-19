
from rest_framework.decorators import api_view , permission_classes
from rest_framework import status
from rest_framework.response import Response
from .serializer import PostSerializer
from ...models import Post
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated , IsAuthenticatedOrReadOnly

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def postList(request):
    
    if request.method == 'GET':
        post = Post.objects.filter(status=True)
        post = PostSerializer(post,many=True)
        return Response(post.data)
    elif request.method == 'POST':
        post = PostSerializer(data=request.data)
        post.is_valid(raise_exception=True)
        post.save()
        return Response(post.data)

@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticated])
def postDetail(request,id):
    post = get_object_or_404(Post,pk=id)
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = PostSerializer(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        post.delete()
        return Response( status=status.HTTP_204_NO_CONTENT)


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
