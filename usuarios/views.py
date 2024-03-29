from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages



def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
      
        
        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, 'Senha e confirmar senha não coincidem')
            return redirect('/usuarios/cadastro')
        
        
        user = User.objects.filter(username=username)
        
        if user.exists():
            messages.add_message(request, constants.ERROR, 'Este usuário já existe, por favor, tente um usuário diferente')
            return redirect('/usuarios/cadastro')
        
        try:
            User.objects.create_user(
                username = username,
                password= senha
            ) 
            messages.add_message(request, constants.SUCCESS, 'Cadastro realizado com sucesso ;)')
            return redirect('/usuarios/login') #Vai dar erro, não criei ainda
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno, por favor, entre em contato com o backend')
            return redirect('/usuarios/cadastro') #redirecionando para cadastro se der erro
        





def login (request):
    return render (request, 'login.html')


def seguranca(request):
    return HttpResponse('Hello World')


    


