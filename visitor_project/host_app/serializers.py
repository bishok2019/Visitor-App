from rest_framework import serializers
from .models import Host, Department
from django.contrib.auth import authenticate


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class HostSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    department = serializers.CharField(required=True)
    
    class Meta:
        model = Host
        fields = ('id', 'username', 'email', 'password','department')
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def create(self, validated_data):
        host = Host.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            # department=validated_data['department']
        )
        return host
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            host = authenticate(username=username, password=password)
            if not host:
                raise serializers.ValidationError('Invalid username or password.')
            if not host.is_active:
                raise serializers.ValidationError('User account is disabled.')
            attrs['host'] = host
            return attrs
        raise serializers.ValidationError('Must include "username" and "password".')
