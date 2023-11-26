from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from veiculo.bibliotecas import LoginObrigatorio
from django.http import FileResponse, Http404
from anuncio.models import Anuncio
from django.urls import reverse_lazy
from anuncio.forms import FormularioAnuncio


class ListarAnuncios(LoginObrigatorio, ListView):
    model = Anuncio
    context_object_name = 'anuncios'
    template_name = 'anuncio/listar.html'

class CriarAnuncios(LoginObrigatorio, CreateView):
    model = Anuncio
    form_class = FormularioAnuncio
    template_name = 'anuncio/novo.html'
    success_url = reverse_lazy('listar-anuncios')

class EditarAnuncios(LoginObrigatorio, UpdateView):
    model = Anuncio
    form_class = FormularioAnuncio
    template_name = 'anuncio/editar.html'
    success_url = reverse_lazy('listar-anuncios')

class DeletarAnuncio(LoginObrigatorio, DeleteView):
    model = Anuncio
    template_name = 'anuncio/deletar.html'
    success_url = reverse_lazy('listar-anuncios')
