from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    TokenBlacklistView,
)
from .views import (
    UserRegisterAPIView,
    MyProfileAPIView,
    # ResetPasswordAPIView,
    # PasswordTokenCheckView,
    # SetNewPasswordAPIView
)

app_name = 'account'

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('api/register/', UserRegisterAPIView.as_view(), name='register'),
    path('api/myprofile/', MyProfileAPIView.as_view(), name='myprofile'),
    # path('api/reset_password/', ResetPasswordAPIView.as_view(), name='resetpassword'),
    # path('api/check_password/<str:uidb64>/<str:token>/', PasswordTokenCheckView.as_view(), name='check_password'),
    # path('api/set_new_password/', SetNewPasswordAPIView.as_view(), name='set_new_password')


]

