from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Bolao_list, name='home'),
#    url(r'^$', views.partidas_list, name='partidas'),
    url(r'^recuperar/$', views.recuperar_list, name='recuperar'),
    url(r'^listaDatas/$', views.listaDatas_list, name='listarDatas'),
    url(r'^jogosDaData/$', views.jogosDaData_list, name='jogos'),
    url(r'^confirmacaoDaAposta/$', views.confirmacaoDaAposta_list, name='confirmacaoDaAposta'),
    url(r'^apostas/$', views.telaApostas_list, name='apostas'),
    url(r'^estatisticas/$', views.estatísticasDaAposta_list, name='estatisticas'),
    url(r'^login/$', views.login_list, name='login'),
    url(r'^logout/$', views.logout_list, name='logout'),
    url(r'^signup/$', views.signup_list, name='signup'),
]
