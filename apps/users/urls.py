from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^login/$', views.login, name='login'),
    url(r'^process_login/$', views.process_login, name='process_login'),
    url(r'^process_register/$', views.process_register, name='process_register'),
    url(r'^register/$', views.register, name='register'),
    url(r'^register/$', views.register, name='register'),
]