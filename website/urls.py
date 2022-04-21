from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('register', views.registerpg, name='register'),
    path('login', views.loginpg, name='login'),
    path('logout', views.logoutpg, name='logout'),
    path('',views.homepg,name='index'),
    path('new_question',views.newquestPage,name='new_question'),
    path('question/<int:id>',views.questPage,name='question'),
    path('reply', views.replyPage, name='reply'),  

]
