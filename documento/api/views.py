
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from documento.api.pagination import  DocumentoPagination
from documento.api.serializers import DocumentoSerializer
from documento.models import Documento
from documento.api.permissions import IsAdminOrReadOnly

class DocumentoListAV(APIView):
    
    permission_classes = [IsAdminOrReadOnly, IsAuthenticated]
    pagination_class = DocumentoPagination
    
    def get(self, request):
        
        documentos = Documento.objects.all()
        serializer = DocumentoSerializer(documentos, many=True, context={'request': request})
        return Response(serializer.data)
    
    def post(self, request):
        
        de_serializer = DocumentoSerializer(data=request.data)
        if de_serializer.is_valid():
            de_serializer.save()
            return Response(de_serializer.data)
        else:
            return Response(de_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DocumentoDetailAV(APIView):
    
    permission_classes = [IsAdminOrReadOnly, IsAuthenticated]
    
    def get(self, request, pk):
        
        try:
            documento = Documento.objects.get(pk=pk)
        except Documento.DoesNotExist:
            message = {'erro': 'Documento não existe'}
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        
        serializer = DocumentoSerializer(documento, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def put(self, request, pk):
        
        try:
            documento = Documento.objects.get(pk=pk)
        except Documento.DoesNotExist:
            message = {'erro': 'Documento não existe'}
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        
        de_serializer = DocumentoSerializer(documento, data=request.data, context={'request': request})
        if de_serializer.is_valid():
            de_serializer.save()
            return Response(de_serializer.data)
        else:
            return Response(de_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        
        try:
            documento = Documento.objects.get(pk=pk)
        except Documento.DoesNotExist:
            message = {'erro': 'Documento não existe'}
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        
        documento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
                