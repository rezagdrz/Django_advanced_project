from django.shortcuts import render

def index_view(request):
    context = {'name':'hasan'}
    return render(request,'index.html',context)
# Create your views here.
