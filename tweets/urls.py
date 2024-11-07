from django.urls import path
from .views import UserRegistrationAPI, Users
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView

)

urlpatterns = [
    path('register',UserRegistrationAPI.as_view(), name="user-register"),
    path('token', TokenObtainPairView.as_view(), name="token_obtain_pair_view"),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh_view'),
    path('users', Users.as_view(), name='get_all_users')
]