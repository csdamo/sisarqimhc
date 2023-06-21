from rest_framework import serializers
from acervo.models import Acervo
from estrutura.api.serializers import EstruturaSerializer
from estrutura.models import Estrutura


class AcervoSerializer(serializers.ModelSerializer):
    
    estrutura_acervo = serializers.SerializerMethodField()
    
    class Meta:
        model = Acervo
        exclude = ('criado_em', 'atualizado_em')
    
    def validate(self, data):
        ordem = data['ordem_exibicao']
        if ordem <= 0:
            raise serializers.ValidationError('Ordem deve ser maior que zero.')
      
        return data
    
    def get_estrutura_acervo(self, instance):
        estrutura_acervo = Estrutura.objects.filter(nivel=1, acervo=instance)
        estrutura_n1 = EstruturaSerializer(estrutura_acervo, many=True).data
        return estrutura_n1
    