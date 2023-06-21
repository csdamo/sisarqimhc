from django.urls import path
from assunto.api.views import AssuntoListAV, AssuntoDetailAV

urlpatterns = [
    path('', AssuntoListAV.as_view(), name='assunto-list'),
    path('<int:pk>/', AssuntoDetailAV.as_view(), name='assunto-detail'),

]