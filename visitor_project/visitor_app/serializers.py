from rest_framework import serializers
from .models import CustomUser, Department, Visitor
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    department = serializers.CharField(required=True)
    
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password','department')
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise serializers.ValidationError('Invalid username or password.')
            if not user.is_active:
                raise serializers.ValidationError('User account is disabled.')
            attrs['user'] = user
            return attrs
        raise serializers.ValidationError('Must include "username" and "password".')

class VisitorSerializer(serializers.ModelSerializer):
    department = serializers.CharField(source='visiting_to.department.name', read_only=True)
    host = serializers.CharField(source='visiting_to.username', read_only=True)
    class Meta:
        model = Visitor
        # fields = '__all__'
        fields = ['name', 'visiting_to', 'meeting_date', 'meeting_time','reason', 'created_at', 'department','host']