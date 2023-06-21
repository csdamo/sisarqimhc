from django.urls import path
from produtor.api.views import ProdutorListAV, ProdutorDetailAV

urlpatterns = [
    path('', ProdutorListAV.as_view(), name='produtor-list'),
    path('<int:pk>/', ProdutorDetailAV.as_view(), name='produtor-detail'),

]