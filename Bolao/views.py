from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Partida
from .models import Jogador

def Bolao_list(request):
    return render(request, 'Bolao/home.html', {})

def partidas_list(request):
    partidas = Partida.objects.filter(data__gt=timezone.now()).order_by('data')
    return render(request, 'Bolao/partidas.html', {'partidas':partidas})

def recuperar_list(request):
    return render(request, 'Bolao/recuperar.html', {})

def login_list(request):
    return render(request, 'Bolao/login.html', {})

def logout_list(request):
    return render(request, 'Bolao/logout.html', {})

def signup_list(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            Jogador.objects.create(nome=username,email=username+'@bolao.com',password=raw_password)
            partidas = Partida.objects.filter(data__gt=timezone.now()).order_by('data')
            jogadores = Jogador.objects.order_by('creditos')
            return render(request, 'partidas.html', {'partidas':partidas, 'jogadores':jogadores})
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def listaDatas_list(request):
    return render(request, 'Bolao/listaDatas.html',{})
def jogosDaData_list(request):
    return render(request,'Bolao/jogosDaData.html',{})
def confirmacaoDaAposta_list(request):
    return render(request,'Bolao/confirmacaoDaAposta.html',{})
def telaApostas_list(request):
    return render(request,'Bolao/telaAposta.html',{})
def estatísticasDaAposta_list(request):
    return render(request,'Bolao/estatisticasDaAposta.html',{})

