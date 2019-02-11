from django.urls import path
from django.conf.urls import url, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('adverts/', views.adverts, name='adverts'),
    path('advert/<id>/', views.advert, name='advert'),
    path('startups/', views.startups, name='startups'),
    path('investors/', views.investors, name='investors'),
    path('profile/<id>/', views.profile, name='profile'),
    url('login_user/', views.login_user, name="login_user"),
    url('logout_user/', views.logout_user, name="logout_user"),
    url('register_user/', views.register_user, name="register_user"),
]
