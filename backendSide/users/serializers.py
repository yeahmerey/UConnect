from rest_framework import serializers 
from .models import UserProfie
from django.contrib.auth.models import User
class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username' , read_only = True)

    class Meta : 
        model = UserProfie 
        fields = ['id' , 'username' , 'bio' , 'avatar']

class RegisterSerializer(serializers.ModelSerializer) : 
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta : 
        model = User 
        fields = ['username', 'email', 'password1', 'password2']

    def validate(self , data):
        if data['password1'] != data['password2'] : 
            raise serializers.ValidationError({"password" : "Passwords do not match."})
        return data

    def create(self , validated_data): 
        validated_data.pop('password2')
        user = User.objects.create_user (
            username = validated_data['username'], 
            email = validated_data['email'],
            password = validated_data['password1'], 
        )

        UserProfie.objects.create(user=user)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()



