from rest_framework import serializers
from estrutura.models import Estrutura


class EstruturaSerializer(serializers.ModelSerializer):
    
    nivel_estrutura = serializers.SerializerMethodField()
    # sub_estruturas = serializers.SerializerMethodField()
    
    class Meta:
        model = Estrutura
        exclude = ('nivel', 'criado_em', 'atualizado_em')
    
    def get_nivel_estrutura(self, instance):
        estrutura = Estrutura.objects.get(pk=instance.pk)
        nivel_estrutura = estrutura.nivel
        return nivel_estrutura
    
    # def get_sub_estruturas(self, instance):
    #     estruturas = Estrutura.objects.filter(estrutura_nivel_superior=instance)
    #     sub_estruturas = EstruturaSerializer(estruturas, many=True).data
    #     return sub_estruturas
    