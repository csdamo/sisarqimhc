from django.urls import path
from pessoa.api.views import PessoaListAV, PessoaDetailAV

urlpatterns = [
    path('', PessoaListAV.as_view(), name='pessoa-list'),
    path('<int:pk>/', PessoaDetailAV.as_view(), name='pessoa-detail'),

]