from django.urls import path
from estrutura import views

urlpatterns = [
    path('lista/', views.lista, name='estrutura-lista'),
    path('<int:id>/', views.detalhe, name='estrutura-detalhe'),
    path('novo/', views.novo, name='estrutura-novo'),
    path('edita/<int:id>', views.edita, name='estrutura-edita'),
    path('deleta/<int:id>', views.deleta, name='estrutura-deleta'),
]
