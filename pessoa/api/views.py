
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from pessoa.api.pagination import PessoaLOPagination, PessoaPagination
from pessoa.api.serializers import PessoaSerializer
from pessoa.models import Pessoa
from pessoa.api.permissions import IsAdminOrReadOnly

class PessoaListAV(APIView):
    
    permission_classes = [IsAdminOrReadOnly, IsAuthenticated]
    pagination_class = PessoaPagination
    
    def get(self, request):
        
        palavra_chave = self.request.query_params.get('palavrachave', None)
        
        pessoas = Pessoa.objects.all()
        
        if palavra_chave:
            pessoas = pessoas.filter(nome__icontains=palavra_chave)
            
        serializer = PessoaSerializer(pessoas, many=True, context={'request': request})
        return Response(serializer.data)
    
    def post(self, request):
        
        de_serializer = PessoaSerializer(data=request.data)
        if de_serializer.is_valid():
            de_serializer.save()
            return Response(de_serializer.data)
        else:
            return Response(de_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PessoaDetailAV(APIView):
    
    permission_classes = [IsAdminOrReadOnly, IsAuthenticated]
    
    def get(self, request, pk):
        
        try:
            pessoa = Pessoa.objects.get(pk=pk)
        except Pessoa.DoesNotExist:
            message = {'erro': 'Pessoa não existe'}
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PessoaSerializer(pessoa, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def put(self, request, pk):
        
        try:
            pessoa = Pessoa.objects.get(pk=pk)
        except Pessoa.DoesNotExist:
            message = {'erro': 'Pessoa não existe'}
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        
        de_serializer = PessoaSerializer(pessoa, data=request.data, context={'request': request})
        if de_serializer.is_valid():
            de_serializer.save()
            return Response(de_serializer.data)
        else:
            return Response(de_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        
        try:
            pessoa = Pessoa.objects.get(pk=pk)
        except Pessoa.DoesNotExist:
            message = {'erro': 'Pessoa não existe'}
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        
        pessoa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
                