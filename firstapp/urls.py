# This file letting the app host it url separately

from django.urls import path
from firstapp import views

# template tagging

app_name = 'firstapp'
urlpatterns = [
    path(r'', views.index, name='index'),

    path(r'registration', views.register, name='register'),
    path(r'logout', views.user_logout, name='user_logout'),
    path(r'login', views.user_login, name='user_login'),
]
