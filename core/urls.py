from operator import index
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.index,name='index' ),
    path('setting', views.setting,name='setting'),
    path('signup', views.signup,name='signup' ),
    path('signin', views.signin,name='signin' ),
    path('logout', views.logout,name='logout' ),
    path('upload', views.upload,name='upload' ),
]