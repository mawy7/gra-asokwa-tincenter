from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'tinadmin'
urlpatterns = [
   	url(r'^register/$', views.register, name='register'),
    
]