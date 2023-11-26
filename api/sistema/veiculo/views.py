from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from veiculo.bibliotecas import LoginObrigatorio
from veiculo.models import Veiculo 
from django.http import FileResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from veiculo.forms import FormularioVeiculo
from django.urls import reverse_lazy
from veiculo.serialize import SerializadorVeiculo
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions


# Create your views here.

class ListarVeiculos(LoginObrigatorio, ListView):
    model = Veiculo
    context_object_name = 'veiculos'
    template_name = 'veiculo/listar.html'

    def get_queryset(self, **kwargs):
        pesquisa = self.request.GET.get('pesquisa', None)
        queryset = Veiculo.objects.all()
        if pesquisa is not None:
            queryset = queryset.filter(modelo__icontains=pesquisa)
        return queryset


class FotoVeiculo(LoginObrigatorio):

    def get(self, request, arquivo):
        try:
            veiculo = Veiculo.objects.get(foto='veiculo/fotos/{}'.format(arquivo))
            return FileResponse(veiculo.foto)
        except ObjectDoesNotExist:
            raise Http404("Foto não encontrada ou acesso não aurotizado!")
        except Exception as exception:
            raise exception
        
class APIListarCriarVeiculos(ListCreateAPIView):
    serializer_class = SerializadorVeiculo    #Transformar os dados em um objeto json
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):        
        return Veiculo.objects.all()
    
class APIObterEditarDeletarVeiculos(RetrieveUpdateDestroyAPIView):
    serializer_class = SerializadorVeiculo
    authentication_classes = [TokenAuthentication]
    permission_casses = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Veiculo.objects.all()
    

class CriarVeiculos(LoginObrigatorio, CreateView):
    model = Veiculo
    form_class = FormularioVeiculo
    template_name = 'veiculo/novo.html'
    success_url = reverse_lazy('listar-veiculos')
    
class EditarVeiculos(LoginObrigatorio, UpdateView):
    model = Veiculo
    form_class = FormularioVeiculo
    template_name = 'veiculo/editar.html'
    success_url = reverse_lazy('listar-veiculos')

class DeletarVeiculo(LoginObrigatorio, DeleteView):
    model = Veiculo
    template_name = 'veiculo/deletar.html'
    success_url = reverse_lazy('listar-veiculos')
