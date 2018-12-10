from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^calc/$', views.calc, name='calc'),
    url(r'^checkout/$', views.checkout, name='checkout'),
]
