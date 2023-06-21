from django.urls import path
from user_app.api.views import get_usuario, registration_view, logout_view,login_view, session_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('login/', login_view, name='login-app'),
    path('register/', registration_view  , name='register'),
    path('logout/', logout_view  , name='logout'),
    path('session/', session_view  , name='session'),
    path('get_usuario/', get_usuario  , name='get_usuario'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
