from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer

class RegisterAPIView(CreateAPIView):

    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if (serializer.is_valid(raise_exception=True)):
            user = serializer.create(serializer.validated_data)
            print(user)
            if (user):
                return Response(status=status.HTTP_200_OK)
        return Response(data={"msg": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)