from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str
from django.utils.http import urlsafe_base64_decode
from rest_framework.response import Response
from rest_framework import generics, views
from .serializers import UserRegisterSerializer, UserSerializer, ResetPasswordSerializer, SetNewPasswordSerializer
from .models import User
from rest_framework.permissions import IsAuthenticated
# from .tasks import send_mail_reset_passwd


class UserRegisterAPIView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()


class MyProfileAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        serializer = self.get_serializer(user)
        return Response(serializer.data)


# class ResetPasswordAPIView(generics.GenericAPIView):
#     serializer_class = ResetPasswordSerializer
#     queryset = User.objects.all()
#
#     def post(self, request, *args, **kwargs):
#         email = User.objects.get(email=request.data['email']).email
#         send_mail_reset_passwd.delay(email)
#         return Response({"detail": "rest link sent your email"})


# class PasswordTokenCheckView(generics.GenericAPIView):
#     serializer_class = ResetPasswordSerializer
#
#     def get(self, request, uidb64, token, *args, **kwargs):
#         try:
#             user_id = smart_str(urlsafe_base64_decode(uidb64))
#             user = User.objects.get(id=user_id)
#             if not PasswordResetTokenGenerator().check_token(user, token):
#                 return Response({'success': False, 'detail': 'Token is not valid, please try again'}, status=406)
#             return Response({'success': True, 'message': 'Successfully checked', 'uidb64': uidb64, 'token': token},
#             status=200)
#         except Exception as e:
#             return Response({'success': False, 'detail': f'{e.args}'}, status=401)


# class SetNewPasswordAPIView(views.APIView):
#     def post(self, request, *args, **kwargs):
#         uidb64 = request.data('uidb64')
#         password2 = request.data.get('password2')
#         _id = force_str(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(id=_id)
#         user.set_password(password2)
#         user.save()
#         return Response({'success': True, 'message': 'Successfully changed password'}, status=200)
