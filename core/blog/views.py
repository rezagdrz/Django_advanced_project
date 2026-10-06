from django.shortcuts import render , get_object_or_404 
from django.urls import reverse
from django.views.generic import TemplateView , RedirectView
from .models import Post
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView
from django.utils import timezone

def index_view(request):
    context = {'name':'hasan'}
    return render(request,'index.html',context)

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'ali shams'
        context['post'] = Post.objects.get(pk=kwargs["pk"])
        return context

class RedirectToDjango(RedirectView):
    pattern_name = 'blog:home-clbv' 
    
    def get_redirect_url(self, *args, **kwargs):
        post =get_object_or_404(Post, pk=kwargs["pk"])
        print(post.category)
        return super().get_redirect_url(self,*args,*kwargs)
    
class PostList(ListView):
    context_object_name = "posts"
    ordering = '-pk'
    model = Post

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context
# Create your views here.
