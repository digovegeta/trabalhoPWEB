from django.shortcuts import render

def Bolao_list(request):
    return render(request, 'Bolao/home.html', {})

def recuperar_list(request):
    return render(request, 'Bolao/recuperar.html', {})
