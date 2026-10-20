from django.urls import path , include
from .views import *

app_name = 'api-v1'
urlpatterns = [
    #path('post/list/',postList,name='post-list'),
    #path('post/detail/<int:id>/',postDetail,name='post-detail'),
    path('post/list/',PostList.as_view(),name='post-list'),
    path('post/detail/<int:pk>/',PostDetail.as_view(),name='post-detail'),
    
]
