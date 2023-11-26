import base64
from drf_extra_fields.fields import Base64ImageField
from veiculo.models import Veiculo
from rest_framework import serializers

class SerializadorVeiculo(serializers.ModelSerializer):
    """
    Serializador para o model Veiculo
    """
    marca_display = serializers.SerializerMethodField()
    cor_display = serializers.SerializerMethodField()
    combustivel_display = serializers.SerializerMethodField()
    foto = Base64ImageField(required= False, represent_in_base64=True)

    class Meta:
        model = Veiculo
        exclude = []

    def get_marca_display(self, instancia):
        return instancia.get_marca_display()

    def get_cor_display(self, instancia):
        return instancia.get_cor_display()

    def get_combustivel_display(self, instancia):
        return instancia.get_combustivel_display()
