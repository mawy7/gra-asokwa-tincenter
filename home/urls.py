from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', view=views.home, name='home'),
    path('summary', view=views.summary, name='summary'),
]