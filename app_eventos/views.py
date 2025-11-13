from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Evento
from django.contrib.auth.decorators import login_required, permission_required

def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        usu = request.POST.get('username')
        pasw = request.POST.get('password')
        usuario = authenticate(request, username=usu, password=pasw)
        if usuario:
            login(request, usuario)
            return redirect ('eventos')
        else:
            return redirect ('login')

@login_required
@permission_required('app_eventos.view_evento')
def eventos_view(request):
    if request.user.is_authenticated:
        eventos = Evento.objects.all()
        return render(request, 'eventos.html', {'eventos': eventos})

    else:
        return redirect ('login')
