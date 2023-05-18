from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista, name='acervo-lista'),
    path('<int:id>/', views.detalhe, name='acervo-detalhe'),
    path('novo/', views.novo, name='acervo-novo'),
    path('edita/<int:id>', views.edita, name='acervo-edita'),
    path('deleta/<int:id>', views.deleta, name='acervo-deleta'),
]
