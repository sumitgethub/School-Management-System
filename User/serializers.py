from urllib3 import Retry
from User.models import Profile, User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

#user register serializers
class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'},write_only = True)
    class Meta:
        model = User
        fields = ('unique_id','email','password','password2')
        extra_kwargs ={
            'password':{'write_only':True}
        }
        # Validating password and conform password while Registration
    def validate(self,attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("password and confirm password doesn't not match")
        return attrs



    def create(self, validate_data):
        return User.objects.create_user(**validate_data)
    
#user login serializer
class UserLoginSerializer(serializers.ModelSerializer):
    unique_id = serializers.CharField(max_length=12)
    class Meta:
        model = User
        fields = ('unique_id','password')