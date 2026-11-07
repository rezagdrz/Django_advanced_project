from django.urls import path , include
from . import views
from rest_framework import routers

app_name = 'api-v1'
urlpatterns = [
    path('registerations/',views.RegistrationsApiViews.as_view(),name='registrations'),
    path('token/login/', views.CustomAuthToken.as_view(),name='token-login'),
    path('token/logout/',views.CustomDiscardToken.as_view(),name='token-logout'),
]
