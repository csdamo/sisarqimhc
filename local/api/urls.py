from django.urls import path
from local.api.views import LocalListAV, LocalDetailAV

urlpatterns = [
    path('', LocalListAV.as_view(), name='local-list'),
    path('<int:pk>/', LocalDetailAV.as_view(), name='local-detail'),

]