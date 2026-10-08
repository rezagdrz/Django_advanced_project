from django.db import models
from django.contrib.auth import get_user_model
'''
these are some class to define Post and Category for app blog 
'''
#User = get_user_model()
class Post(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(null=True,blank=True)
    content = models.TextField()
    author = models.ForeignKey('accounts.Profile',on_delete=models.CASCADE ,default= 1 )
    status = models.BooleanField()
    category = models.ForeignKey('Category',on_delete=models.SET_NULL,null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField()
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
# Create your models here.
