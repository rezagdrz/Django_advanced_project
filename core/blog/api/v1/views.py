
from rest_framework.decorators import api_view , permission_classes , action
from rest_framework import status
from rest_framework.response import Response
from .serializer import PostSerializer , CategorySerializer
from ...models import Post , Category
from accounts.models import Profile , User
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated , IsAuthenticatedOrReadOnly 
from .permissions import AuthorAllStaffAllButEditOrReadOnly
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView , ListCreateAPIView , RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin , RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin , CreateModelMixin
from rest_framework import viewsets
from rest_framework.permissions import BasePermission
from rest_framework.filters import SearchFilter 
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.filters import SearchFilter , OrderingFilter
from .pagination import *
"""
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
@api_view()
def postDetail(request,id):
    try:
        post = Post.objects.get(pk=id)
        post = PostSerializer(post)
        return Response(post.data)
    
    except Post.DoesNotExist:
        return Response({'datail':'this post does not exist'},status=status.HTTP_404_NOT_FOUND)


class PostList(ListCreateAPIView):
    '''a class for getting and creating posts'''
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class =PostSerializer
    queryset = Post.objects.filter(status=True)



class PostDetail(RetrieveUpdateDestroyAPIView):
    '''a class for getting post detail and edit and removing it'''
    permission_classes = [IsAuthenticated]
    serializer_class =PostSerializer
    queryset = Post.objects.filter(status=True)

class PostListViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class =PostSerializer
    queryset = Post.objects.filter(status=True)
    def list(self,requset):
        queryset = Post.objects.filter(status=True)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class PostDetailViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class =PostSerializer
    queryset = Post.objects.filter(status=True)

    def retrieve(self,request, pk=None):
        post = get_object_or_404(self.queryset,pk=pk)
        serializer = self.serializer_class(post)
        return Response(serializer.data)
    
    def update(self,request, pk=None):
        post = get_object_or_404(self.queryset,pk=pk)
        serializer = self.serializer_class(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self,request, pk=None):
        post = get_object_or_404(self.queryset,pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""

class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = [AuthorAllStaffAllButEditOrReadOnly ]
    serializer_class =PostSerializer
    queryset = Post.objects.filter(status=True)
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields = ['category','author']
    search_fields = ['title', 'content']
    ordering_fields = ['published_date']
    pagination_class = CustomPagination
    pagination_class.page_size = 5
    
    # def perform_create(self, serializer):
    #     serializer.save(author=Profile.objects.get(user=self.request.user))

    @action(detail=False,methods=['get'])
    def get_last_post(self,request):
        post =Post.objects.filter(status=True).order_by('-id').first()
        if post is None:
            return Response({'detail':'there are no posts '},status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(post)
        return Response(serializer.data)
    
class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class =CategorySerializer
    queryset = Category.objects.all()
    

    