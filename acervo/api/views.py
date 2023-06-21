
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from acervo.api.pagination import AcervoLOPagination, AcervoPagination
from acervo.api.serializers import AcervoSerializer
from acervo.models import Acervo
from acervo.api.permissions import IsAdminOrReadOnly

class AcervoListAV(APIView):
    
    permission_classes = [IsAdminOrReadOnly, IsAuthenticated]
    pagination_class = AcervoPagination
    
    def get(self, request):
        
        acervos = Acervo.objects.all()
        serializer = AcervoSerializer(acervos, many=True, context={'request': request})
        return Response(serializer.data)
    
    def post(self, request):
        
        de_serializer = AcervoSerializer(data=request.data)
        if de_serializer.is_valid():
            de_serializer.save()
            return Response(de_serializer.data)
        else:
            return Response(de_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AcervoDetailAV(APIView):
    
    permission_classes = [IsAdminOrReadOnly, IsAuthenticated]
    
    def get(self, request, pk):
        
        try:
            acervo = Acervo.objects.get(pk=pk)
        except Acervo.DoesNotExist:
            message = {'erro': 'Acervo não existe'}
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        
        serializer = AcervoSerializer(acervo, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def put(self, request, pk):
        
        try:
            acervo = Acervo.objects.get(pk=pk)
        except Acervo.DoesNotExist:
            message = {'erro': 'Acervo não existe'}
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        
        de_serializer = AcervoSerializer(acervo, data=request.data, context={'request': request})
        if de_serializer.is_valid():
            de_serializer.save()
            return Response(de_serializer.data)
        else:
            return Response(de_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        
        try:
            acervo = Acervo.objects.get(pk=pk)
        except Acervo.DoesNotExist:
            message = {'erro': 'Acervo não existe'}
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        
        acervo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
                