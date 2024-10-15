from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status

from django.contrib.auth import login

from .serializers import RegisterSerializer

class RegisterAPIView(CreateAPIView):

    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if (serializer.is_valid(raise_exception=True)):
            user = serializer.create(serializer.validated_data)
            print(user)
            if (user):
                return Response(status=status.HTTP_201_CREATED)
        return Response(data={"msg": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)
    

class LoginAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        JWT_authenticator = JWTAuthentication()
        user = JWT_authenticator.authenticate(request=request)[0]       # returns tuple
        if (user is not None):
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)