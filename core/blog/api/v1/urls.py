from django.urls import path , include
from .views import *

app_name = 'api-v1'
urlpatterns = [
    path('post/list/',postList,name='post-list'),
    path('post/detail/<int:id>/',postDetail,name='post-detail'),
]
