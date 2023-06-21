from rest_framework import serializers
from local.models import Local


class LocalSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Local
        exclude = ('criado_em', 'atualizado_em')

    