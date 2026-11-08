from django.urls import path , include
from . import views
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'api-v1'
urlpatterns = [
    path('registerations/',views.RegistrationsApiViews.as_view(),name='registrations'),
    #token
    path('token/login/', views.CustomAuthToken.as_view(),name='token-login'),
    path('token/logout/',views.CustomDiscardToken.as_view(),name='token-logout'),
    #JWT
    path('jwt/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
