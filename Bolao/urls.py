from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Bolao_list, name='home'),
    url(r'^recuperar/$', views.recuperar_list, name='recuperar'),
]
