from django.shortcuts import render , get_object_or_404 
from django.urls import reverse
from django.views.generic import TemplateView , RedirectView , UpdateView , DeleteView
from .models import Post
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.views.generic.edit import FormView
from .forms import PostForm
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin , PermissionRequiredMixin

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
    
class PostList(LoginRequiredMixin,ListView):
    context_object_name = "posts"
    paginate_by = 3
    ordering = '-pk'
    model = Post

class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post
    context_object_name = 'post'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context

class PostCreate(FormView):
    template_name = "blog/contact.html"
    form_class = PostForm
    success_url = "/post/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    success_url = '/post/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostEditView(PermissionRequiredMixin,UpdateView):
    model = Post
    form_class = PostForm
    success_url = '/post/' 
    permission_required = 'post.edit_choice'

class PostDeleteView(PermissionRequiredMixin,DeleteView):
    model = Post
    success_url = '/post/'
    permission_required = 'post.delete_choice'
# Create your views here.
