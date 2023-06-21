from rest_framework.decorators import api_view, permission_classes
from rest_framework.fields import NOT_READ_ONLY_REQUIRED
from rest_framework.response import Response
from user_app.api.serializers import RegistrationSerializer
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.contrib import auth
from user_app.models import Account


@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def session_view(request):
    if request.method == 'GET':
        user = request.user
        account = Account.objects.get(email=user)
        data = {}
        if account is not None:
            data['response'] = 'O usuário está na sessão'
            data['username'] = account.username
            data['id'] = account.id
            data['email'] = account.email
            data['first_name'] = account.first_name
            data['last_name'] = account.last_name
            data['phone_number'] = account.phone_number
            data['cpf'] = account.cpf
            data['is_staff'] = account.is_staff
            data['is_admin'] = account.is_admin
            refresh = RefreshToken.for_user(account)
            data['token'] = {
                'refresh' : str(refresh),
                'access': str(refresh.access_token)
            }
            return Response(data)
        else:
            data['error'] = 'Usuário não existe'
            return Response(data, status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST',])
def logout_view(request):
    if request.method == 'POST':
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST',])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'Usuário criado com sucesso'
            data['username'] = account.username
            data['id'] = account.id
            data['email'] = account.email
            data['first_name'] = account.first_name
            data['last_name'] = account.last_name
            data['phone_number'] = account.phone_number
            data['cpf'] = account.cpf
            data['is_staff'] = account.is_staff
            data['is_admin'] = account.is_admin
            refresh = RefreshToken.for_user(account)
            data['token'] = {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }
            return Response(data)

        else:
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def login_view(request):
    data = {}
    if request.method=='POST':
        email = request.data.get('email')
        password = request.data.get('password')
        account = auth.authenticate(email=email, password=password)
        if account is not None:
            data['response']='Login efetuado com sucesso'
            data['username']=account.username
            data['id']=account.id
            data['email']=account.email
            data['first_name']=account.first_name
            data['last_name']=account.last_name
            data['phone_number']=account.phone_number
            data['cpf'] = account.cpf
            data['is_staff'] = account.is_staff
            data['is_admin'] = account.is_admin
            refresh = RefreshToken.for_user(account)
            data['token'] = {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }
            return Response(data)
        else:
            data['error'] = "Credenciais incorretas"
            return Response(data, status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET',])
def get_usuario(request):
    
    data = {}
    if request.method == 'GET':
        
        if request.GET.get('usuario_id'):
            usuario_id = request.GET.get('usuario_id')
            account = Account.objects.get(id=usuario_id)
            data_usuario = {}
            if account is not None:
                data_usuario['username'] = account.username
                data_usuario['id'] = account.id
                data_usuario['email'] = account.email
                data_usuario['first_name'] = account.first_name
                data_usuario['last_name'] = account.last_name
                data_usuario['phone_number'] = account.phone_number
                data_usuario['cpf'] = account.cpf
                data['is_staff'] = account.is_staff
                data['is_admin'] = account.is_admin
                refresh = RefreshToken.for_user(account)
                data_usuario['token'] = {
                    'refresh' : str(refresh),
                    'access': str(refresh.access_token)
                }
                data['usuario'] = data_usuario
                return Response(data)
            else:
                data['error'] = 'Usuário não existe'
                return Response(data, status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
                data['error'] = 'Informe usuario_id'
                return Response(data, status.HTTP_500_INTERNAL_SERVER_ERROR)

