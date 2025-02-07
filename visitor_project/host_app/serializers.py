#host-app.serializers.py
from rest_framework import serializers
from .models import Host, Department
from django.contrib.auth import authenticate

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class HostSerializer(serializers.ModelSerializer):
    # username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    # department = serializers.CharField(required=True)
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(), required=True)
    
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
            department=validated_data['department']
        )
        return host
    
class LoginSerializer(serializers.Serializer):
    # username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(email=email, password=password)

            if not user:
                raise serializers.ValidationError('Invalid email or password.')
            if not user.is_active:
                raise serializers.ValidationError('User account is disabled.')
            attrs['user'] = user
            return attrs
        raise serializers.ValidationError('Must include "email" and "password".')
