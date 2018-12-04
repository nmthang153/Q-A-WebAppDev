from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('list/', views.list, name='list'),
    path('add/', views.add, name='add'),
    path('session/<int:sid>', views.showSession, name='session'),
    path('question/<int:id>', views.showQuestion, name='question'),
    path('myquestions', views.myquestions, name='myquestions'),
]
