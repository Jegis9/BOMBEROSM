# importar modulos para funcion
from django.shortcuts import render, redirect
# permite la creacion de formularios determinados por DJANGO
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# modelos para la creacion de usuarios
from django.contrib.auth.models import User
# respuesta para dar al crear el usuario
from django.http import HttpResponse
# creacion de cookie para cuando el usuario se registre
from django.contrib.auth import login, logout, authenticate
# manejo de errores de integridad
from django.db import IntegrityError
# views.py
from django.shortcuts import render




def index(request): 
    return render (request, "pages/index.html")


def signup(request):

    if request.method == 'GET':
            return render (request, 'pages/signUp.html',{
        'form': UserCreationForm
    })
    else:
        #  verifica contraseñas
         if request.POST['password1'] == request.POST['password2']:
            try:  
                user = User.objects.create_user(username=request.POST['username'],
                password=request.POST['password1'])
                user.save()
                # guardar inicio de sesion en la cookie
                login(request, user)
                return redirect('personal')
            except IntegrityError:
                                # muestran mensaje de error o existo si segun los diferentes errores que se podran manejar renderizando la pagina principal
                return render (request, 'pages/signUp.html',{
                'form': UserCreationForm,
                'error': 'Nombre de usuario existente'})
                            # muestran mensaje de error o existo si segun los diferentes errores que se podran manejar renderizando la pagina principal
         return render (request, 'pages/signUp.html',{
        'form': UserCreationForm,
        'error': 'Las contraseñas no coinciden'})
         
         


def navBar(request):
    return render(request, 'navBar.html')

def personal(request):
    return render(request, 'personal.html')

def reportes(request):
    return render(request,'pages/reportes.html' )






def signout(request):
    logout(request)
    return redirect('index')

def personal(request):
    return render(request,'pages/personal.html')

def signin(request):
    
    if request.method == 'GET':
        return render(request,'pages/signin.html',{
            'form': AuthenticationForm
        })
    else:
        
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        
        
        if user is None:
            
            return render(request,'pages/signin.html',{
                'form': AuthenticationForm,
                'error': 'usuario contraseña incorrecto'
            })
        else:
            login(request,user)
            return redirect('personal')

              
          
          
        
