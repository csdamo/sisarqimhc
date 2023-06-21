
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from produtor.api.pagination import ProdutorLOPagination, ProdutorPagination
from produtor.api.serializers import ProdutorSerializer
from produtor.models import Produtor
from produtor.api.permissions import IsAdminOrReadOnly

class ProdutorListAV(APIView):
    
    permission_classes = [IsAdminOrReadOnly, IsAuthenticated]
    pagination_class = ProdutorPagination
    
    def get(self, request):
        
        palavra_chave = self.request.query_params.get('palavrachave', None)
        
        produtores = Produtor.objects.all()
        
        if palavra_chave:
            produtores = produtores.filter(titulo__icontains=palavra_chave)
            
        serializer = ProdutorSerializer(produtores, many=True, context={'request': request})
        return Response(serializer.data)
    
    def post(self, request):
        
        de_serializer = ProdutorSerializer(data=request.data)
        if de_serializer.is_valid():
            de_serializer.save()
            return Response(de_serializer.data)
        else:
            return Response(de_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProdutorDetailAV(APIView):
    
    permission_classes = [IsAdminOrReadOnly, IsAuthenticated]
    
    def get(self, request, pk):
        
        try:
            produtor = Produtor.objects.get(pk=pk)
        except Produtor.DoesNotExist:
            message = {'erro': 'Produtor não existe'}
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProdutorSerializer(produtor, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def put(self, request, pk):
        
        try:
            produtor = Produtor.objects.get(pk=pk)
        except Produtor.DoesNotExist:
            message = {'erro': 'Produtor não existe'}
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        
        de_serializer = ProdutorSerializer(produtor, data=request.data, context={'request': request})
        if de_serializer.is_valid():
            de_serializer.save()
            return Response(de_serializer.data)
        else:
            return Response(de_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        
        try:
            produtor = Produtor.objects.get(pk=pk)
        except Produtor.DoesNotExist:
            message = {'erro': 'Produtor não existe'}
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        
        produtor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
                