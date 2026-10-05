from django.urls import path
from .views import index_view , IndexView , RedirectToDjango
from django.views.generic.base import RedirectView

app_name = 'blog'

urlpatterns = [
    path('home-def/', index_view , name='home-def'),
    #path('home-clb/',TemplateView.as_view(template_name ='index.html',extra_context = {'name':"ali"}))
    path('home-clbv/<int:pk>', IndexView.as_view(),name='home-clbv'),
    
    path("go-to-django/<int:pk>",RedirectToDjango.as_view(),name="go-to-django",),
]
