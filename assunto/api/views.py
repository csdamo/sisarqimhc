
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from assunto.api.pagination import AssuntoPagination
from assunto.api.serializers import AssuntoSerializer
from assunto.models import Assunto
from assunto.api.permissions import IsAdminOrReadOnly

class AssuntoListAV(APIView):
    
    permission_classes = [IsAdminOrReadOnly, IsAuthenticated]
    pagination_class = AssuntoPagination
    
    def get(self, request):
        
        palavra_chave = self.request.query_params.get('palavrachave', None)
        
        assuntos = Assunto.objects.all()
        
        if palavra_chave:
            assuntos = assuntos.filter(titulo__icontains=palavra_chave)
            
        serializer = AssuntoSerializer(assuntos, many=True, context={'request': request})
        return Response(serializer.data)
    
    def post(self, request):
        
        de_serializer = AssuntoSerializer(data=request.data)
        if de_serializer.is_valid():
            de_serializer.save()
            return Response(de_serializer.data)
        else:
            return Response(de_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AssuntoDetailAV(APIView):
    
    permission_classes = [IsAdminOrReadOnly, IsAuthenticated]
    
    def get(self, request, pk):
        
        try:
            assunto = Assunto.objects.get(pk=pk)
        except Assunto.DoesNotExist:
            message = {'erro': 'Assunto não existe'}
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        
        serializer = AssuntoSerializer(assunto, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def put(self, request, pk):
        
        try:
            assunto = Assunto.objects.get(pk=pk)
        except Assunto.DoesNotExist:
            message = {'erro': 'Assunto não existe'}
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        
        de_serializer = AssuntoSerializer(assunto, data=request.data, context={'request': request})
        if de_serializer.is_valid():
            de_serializer.save()
            return Response(de_serializer.data)
        else:
            return Response(de_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        
        try:
            assunto = Assunto.objects.get(pk=pk)
        except Assunto.DoesNotExist:
            message = {'erro': 'Assunto não existe'}
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        
        assunto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
                