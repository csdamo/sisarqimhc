from django.urls import path
from estrutura.api.views import EstruturaListAV, EstruturaDetailAV

urlpatterns = [
    path('', EstruturaListAV.as_view(), name='estrutura-list'),
    path('<int:pk>/', EstruturaDetailAV.as_view(), name='estrutura-detail'),
]
