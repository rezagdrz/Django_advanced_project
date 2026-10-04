from django.urls import path
from .views import index_view
from django.views.generic import TemplateView

urlpatterns = [
    path('home-def/', index_view , name='home'),
    path('home-clb/',TemplateView.as_view(template_name ='index.html',extra_context = {'name':"ali"}))
]
