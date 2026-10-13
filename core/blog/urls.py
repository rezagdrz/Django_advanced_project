from django.urls import path
from .views import *
app_name = 'blog'

urlpatterns = [
    path('home-def/', index_view , name='home-def'),
    path('home-clbv/<int:pk>', IndexView.as_view(),name='home-clbv'),
    path("go-to-django/<int:pk>",RedirectToDjango.as_view(),name="go-to-django",),
    path('post/',PostList.as_view(),name="post_list"),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('post/create/',PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/edit/',PostEditView.as_view(),name='post-edit'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
    path('post/api_view',api_index_view,name='api_view'),
]
