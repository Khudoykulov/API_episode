from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str
from django.utils.http import urlsafe_base64_decode
from rest_framework.response import Response
from rest_framework import generics
from .serializers import UserRegisterSerializer, UserSerializer, ResetPasswordSerializer, SetNewPassworSerializer
from .models import User
from rest_framework.permissions import IsAuthenticated
from .tasks import send_mail_reset_passwd


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


class ResetPasswordAPIView(generics.GenericAPIView):
    serializer_class = ResetPasswordSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        user = User.objects.get(email=request.data['email'])
        send_mail_reset_passwd.delay((user,))
        return Response({"detail": "rest link sent your email"})


class PasswordTokenCheckView(generics.GenericAPIView):

    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            user_id = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=user_id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({'success': False, 'detail': 'Token is not valid, please try again'}, status=406)
            return Response({'success':True, 'message': 'Successfully checked', 'uidb64': uidb64, 'token': token}, status=200)
        except Exception as e:
            return Response({'success': False, 'detail': f'{e.args}'}, status=401)


class SetNewPasswordAPIView(generics.GenericAPIView):
    serializer_class = SetNewPassworSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            return Response({'success': True, 'message': 'Successfully changed password'}, status=200)
        return Response({'success': False, 'message': 'Credentials is invalid'}, status=406)
