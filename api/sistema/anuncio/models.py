from django.db import models
from datetime import datetime
from veiculo.models import Veiculo
from django.contrib.auth.models import User

class Anuncio(models.Model):
    data = models.DateField(auto_now_add=True)
    preco = models.DecimalField(decimal_places=2, max_digits=10)
    descricao = models.CharField(max_length=500)
    veiculo = models.ForeignKey(Veiculo, related_name='anuncios', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, related_name='anuncios_realizados', on_delete=models.CASCADE)

    def __str__(self):
        return '{0} - {1} - ({2})'.format(
            self.data,
            self.veiculo,
            self.usuario
        )
    

