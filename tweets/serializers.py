from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Tweets


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        

    def create(self, validated_data): # I override the create method add some custom logic.
        user = User.objects.create_user(
            username= validated_data['username'],
            email= validated_data['email'],
            password= validated_data['password']
        )
    
        return user
    

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweets
        fields = ['id', 'user', 'content', 'created_at', 'updated_at']
        read_only_fields = ['user', 'created_at', 'updated_at']
    
