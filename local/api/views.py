
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from local.api.pagination import LocalPagination
from local.api.serializers import LocalSerializer
from local.models import Local
from local.api.permissions import IsAdminOrReadOnly

class LocalListAV(APIView):
    
    permission_classes = [IsAdminOrReadOnly, IsAuthenticated]
    pagination_class = LocalPagination
    
    def get(self, request):
        
        palavra_chave = self.request.query_params.get('palavrachave', None)
        
        locais = Local.objects.all()
        
        if palavra_chave:
            locais = locais.filter(titulo__icontains=palavra_chave)
            
        serializer = LocalSerializer(locais, many=True, context={'request': request})
        return Response(serializer.data)
    
    def post(self, request):
        
        de_serializer = LocalSerializer(data=request.data)
        if de_serializer.is_valid():
            de_serializer.save()
            return Response(de_serializer.data)
        else:
            return Response(de_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LocalDetailAV(APIView):
    
    permission_classes = [IsAdminOrReadOnly, IsAuthenticated]
    
    def get(self, request, pk):
        
        try:
            local = Local.objects.get(pk=pk)
        except Local.DoesNotExist:
            message = {'erro': 'Local não existe'}
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        
        serializer = LocalSerializer(local, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def put(self, request, pk):
        
        try:
            local = Local.objects.get(pk=pk)
        except Local.DoesNotExist:
            message = {'erro': 'Local não existe'}
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        
        de_serializer = LocalSerializer(local, data=request.data, context={'request': request})
        if de_serializer.is_valid():
            de_serializer.save()
            return Response(de_serializer.data)
        else:
            return Response(de_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        
        try:
            local = Local.objects.get(pk=pk)
        except Local.DoesNotExist:
            message = {'erro': 'Local não existe'}
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        
        local.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
                