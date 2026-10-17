from django.shortcuts import render , get_object_or_404  
from django.urls import reverse
from django.views.generic import TemplateView , RedirectView , UpdateView , DeleteView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.views.generic.edit import FormView
from .forms import PostForm
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin , PermissionRequiredMixin

data = {
    'name': 'ali',
    'age':21,
    'id':2,
    'city':'tehran'

}

@api_view()
def api_index_view(request):
    return Response(data)
# Create your views here.
