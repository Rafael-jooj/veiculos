from django.urls import path
from veiculo.views import FotoVeiculo, ListarVeiculos, APIListarCriarVeiculos, APIObterEditarDeletarVeiculos, CriarVeiculos, EditarVeiculos, DeletarVeiculo

urlpatterns = [
    path('', ListarVeiculos.as_view(), name='listar-veiculos'),
    path('api/', APIListarCriarVeiculos.as_view(), name='api-listar-veiculos'),
    path('api/<int:pk>/', APIObterEditarDeletarVeiculos.as_view(), name='api-obter-editar-deletar'),
    path('fotos/<str:arquivo>/', FotoVeiculo.as_view(), name='foto-veiculo'),
    path('novo/', CriarVeiculos.as_view(), name='criar-veiculos'),
    path('<int:pk>/', EditarVeiculos.as_view(), name='editar-veiculos'),
    path('deletar/<int:pk>/', DeletarVeiculo.as_view(), name='deletar-veiculo'),
]