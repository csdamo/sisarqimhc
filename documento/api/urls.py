from django.urls import path
from documento.api.views import DocumentoListAV, DocumentoDetailAV

urlpatterns = [
    path('', DocumentoListAV.as_view(), name='documento-list'),
    path('<int:pk>/', DocumentoDetailAV.as_view(), name='documento-detail'),

]