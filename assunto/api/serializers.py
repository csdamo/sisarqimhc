from rest_framework import serializers
from assunto.models import Assunto


class AssuntoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Assunto
        exclude = ('criado_em', 'atualizado_em')

    