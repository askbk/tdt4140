from django.urls import path
from django.conf.urls import url, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('content/<id>/', views.content, name='content'),
    path('adverts/', views.adverts, name='adverts'),
    path('advert/<id>/', views.advert, name='advert'),
    path('startups/', views.startups, name='startups'),
    path('investors/', views.investors, name='investors'),
    path('profile/<id>/', views.profile, name='profile'),
    url('login_user/', views.login_user, name="login_user"),
    url('logout_user/', views.logout_user, name="logout_user"),
    path('register/', views.register, name="register"),
    path('register_startup/', views.register_startup, name="register_startup"),
    path('register_person/', views.register_person, name="register_person"),
    path('register_investor/', views.register_investor, name="register_investor"),
]
