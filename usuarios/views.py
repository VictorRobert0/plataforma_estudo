from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User



def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        
        if not senha == confirmar_senha:
            return redirect('/usuarios/cadastro')
        
        
        user = User.objects.filter(username=username)
        
        if user.exists():
            return redirect('/usuarios/cadastro')
        
        User.objects.create_user(
            username = username,
            password= senha
        ) 
        
        
        return HttpResponse("Teste")




def login (request):
    return render (request, 'login.html')


def seguranca(request):
    return HttpResponse('Hello World')


    


