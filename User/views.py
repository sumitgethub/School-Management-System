from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from User.serializers import UserLoginSerializer, UserRegistrationSerializer
from User.utils import get_custom_jwt_token
from django.contrib.auth import authenticate
# Create your views here.
class UserRegistrationView(APIView):


    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            User = serializer.save()
            token = get_custom_jwt_token(User)
            return Response({'token': token, 'msg': 'Registration Success'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#user login api
class UserLoginView(APIView):


    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            unique_id = serializer.data.get('unique_id')
            password = serializer.data.get('password')
            user = authenticate(unique_id=unique_id, password=password)
            if user is not None:
                token = get_custom_jwt_token(user)
                return Response({'token': token, 'msg': 'Login Success'}, status=status.HTTP_200_OK)
            return Response({'error': {'non_field_errors': ['unique_id or password is not valid']}}, status=status.HTTP_400_BAD_REQUEST)