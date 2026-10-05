from django.shortcuts import render , get_object_or_404 
from django.urls import reverse
from django.views.generic import TemplateView , RedirectView
from .models import Post
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
    
    def get_redirect_url(self, *args, **kwargs):
        post =get_object_or_404(Post, pk=kwargs["pk"])
        print(post.category)
        return reverse('blog:home-clbv' ,kwargs ={'pk': post.pk } )

# Create your views here.
