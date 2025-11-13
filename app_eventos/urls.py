from django.urls import path
from django.shortcuts import redirect
from . import views
from django.http import HttpResponse

urlpatterns = [
    path('', lambda request: redirect('login'), name='home'),
    path('login/', views.login_view, name='login'),
    path('eventos/', views.eventos_view, name='eventos'),
]