from django.urls import path
from acervo.api.views import AcervoListAV, AcervoDetailAV

urlpatterns = [
    path('', AcervoListAV.as_view(), name='acervo-list'),
    path('<int:pk>/', AcervoDetailAV.as_view(), name='acervo-detail'),

]