from django.conf.urls import url, include

from attendance import views

app_name = 'attendance'
urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^api/$', views.mcc_api, name='api'),
]
