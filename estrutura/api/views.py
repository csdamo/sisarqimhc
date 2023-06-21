
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from estrutura.api.serializers import EstruturaSerializer
from estrutura.models import Estrutura


class EstruturaListAV(APIView):
    
    def get(self, request):
        
        acervo_id = self.request.query_params.get('acervo_id', None)
        estrutura_id = self.request.query_params.get('estrutura_superior_id', None)
  
        if acervo_id:
            estruturas = Estrutura.objects.filter(acervo=acervo_id, nivel=1)
            serializer = EstruturaSerializer(estruturas, many=True, context={'request': request})
            return Response(serializer.data)
        
        elif estrutura_id:
            estruturas = Estrutura.objects.filter(estrutura_nivel_superior=estrutura_id)
            serializer = EstruturaSerializer(estruturas, many=True, context={'request': request})
            return Response(serializer.data)
        
        else:
            message = {"erro": "Parâmetro 'acervo_id' ou 'estrutura_superior_id' deve ser informado"}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request):
        
        de_serializer = EstruturaSerializer(data=request.data)
        estrutura_superior_id = self.request.data.get("estrutura_nivel_superior")
        if estrutura_superior_id:
            estrutura_superior = Estrutura.objects.get(pk=estrutura_superior_id)
            nivel_estrutura_superior = estrutura_superior.nivel
        else:
            nivel_estrutura_superior = 0
        
        if de_serializer.is_valid():
            de_serializer.validated_data['nivel'] = int(nivel_estrutura_superior) + 1
            de_serializer.save()
            return Response(de_serializer.data)
        else:
            return Response(de_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EstruturaDetailAV(APIView):
    
    def get(self, request, pk):
        
        try:
            estrutura = Estrutura.objects.get(pk=pk)
        except Estrutura.DoesNotExist:
            message = {'erro': 'Estrutura não existe'}
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EstruturaSerializer(estrutura)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def put(self, request, pk):
        
        try:
            estrutura = Estrutura.objects.get(pk=pk)
        except Estrutura.DoesNotExist:
            message = {'erro': 'Estrutura não existe'}
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        
        de_serializer = EstruturaSerializer(estrutura, data=request.data)
        if de_serializer.is_valid():
            de_serializer.save()
            return Response(de_serializer.data)
        else:
            return Response(de_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        
        try:
            estrutura = Estrutura.objects.get(pk=pk)
        except Estrutura.DoesNotExist:
            message = {'erro': 'Estrutura não existe'}
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        
        estrutura.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
                
