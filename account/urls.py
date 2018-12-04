from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('accounts/login/', auth_views.login, {'template_name': 'auth/login.html'}, name='login'),
    path('accounts/logout/', auth_views.logout, {'next_page': '../login'}, name='logout'),
    path('index/', views.index, name='index'),
    path('profile/<int:id>', views.showProfile, name='profile'),
    path('userm', views.userm, name='userm'),
    path('adduser', views.adduser, name='adduser'),

]
