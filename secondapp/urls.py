from django.urls import path
from secondapp import views

app_name = 'secondapp'
urlpatterns = [
    path('help/', views.index, name='help'),
    path('blog/', views.blog, name='blog'),
]
