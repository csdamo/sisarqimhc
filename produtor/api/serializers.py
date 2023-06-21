from rest_framework import serializers
from produtor.models import Produtor


class ProdutorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Produtor
        exclude = ('criado_em', 'atualizado_em')

    