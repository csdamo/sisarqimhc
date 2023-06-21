from rest_framework import serializers
from pessoa.models import Pessoa


class PessoaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Pessoa
        exclude = ('criado_em', 'atualizado_em')

    