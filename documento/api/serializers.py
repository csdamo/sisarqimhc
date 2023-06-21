from rest_framework import serializers
from documento.models import Documento


class DocumentoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Documento
        exclude = ('criado_em', 'atualizado_em')
