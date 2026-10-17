from django.urls import path , include
from .views import *
app_name = 'blog'

urlpatterns = [
    path('post/api_view/',api_index_view,name='api_view'),
    path('api/v1/',include('blog.api.v1.urls'))
]
