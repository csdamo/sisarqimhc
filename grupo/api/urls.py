from rest_framework.routers import DefaultRouter
from django.urls import include, path
from grupo.api import views

router = DefaultRouter()
router.register('', views.GroupViewSet, basename='group')

urlpatterns = [
    
    path('', include(router.urls))
]
