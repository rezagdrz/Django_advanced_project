from django.contrib import admin
from .models import Post , Category

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','status','created_date','published_date','category']
    list_filter = ['status','category']

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
# Register your models here.
