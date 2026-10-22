from django.urls import path , include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('post',PostModelViewSet,basename='post')
router.register('category',CategoryModelViewSet,basename='category')
urlpatterns = router.urls
app_name = 'api-v1'
# urlpatterns = [
#     #path('post/list/',postList,name='post-list'),
#     #path('post/detail/<int:id>/',postDetail,name='post-detail'),
#     #path('post/list/',PostList.as_view(),name='post-list'),
#     #path('post/detail/<int:pk>/',PostDetail.as_view(),name='post-detail'),
#     # path('post/',PostListViewSet.as_view({'get':'list','post':'create'}),name='post-list'),
#     # path('post/<int:pk>/',PostDetailViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'}),name='post-detail'),
# ]

