# -*- coding: utf-8 -*-
from django.views.generic import View
from django.shortcuts import render, redirect
from django.http import HttpResponse
import logging
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from rest_framework.authtoken.views import  ObtainAuthToken
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


logger = logging.getLogger('sistema')

class Login(View):

    def get(self, request):
        contexto = {'menssagem': ''}
        
        if not request.user.is_authenticated:
            return render(request, 'autenticacao.html', contexto)
        else:
            return redirect("/veiculo")
        
    def post(self, request):
        email = request.POST.get('email', None)
        senha = request.POST.get('password', None)

        user = authenticate(request, username=email, password=senha)
        if user is not None:

            if user.is_active:
                login(request, user)
                return HttpResponse('Bem vindo')

            return render(request, 'autenticacao.html', {'mensagem': 'usuário inativo'})
        
        return render(request, 'autenticacao.html', {'mensagem': 'usuário ou senha inválidos'})
    
class Logout(View):
    def get(self, request):
        logout(request)
        return redirect(settings.LOGIN_URL)
    
class LoginApi(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data,
            context={
                'request': request
            }
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'id': user.id,
            'nome': user.first_name,
            'email': user.email,
            'token': token.key
        })