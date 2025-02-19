#host-app.serializers.py
from rest_framework import serializers
from .models import Host, Department
from django.contrib.auth import authenticate
from visitor_app.models import Visitor

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class HostSerializer(serializers.ModelSerializer):
    # username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    # department = serializers.CharField(required=True)
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(), required=True, write_only = True)
    depart = serializers.CharField(source='department.name', read_only=True)
    
    class Meta:
        model = Host
        fields = ('id', 'username', 'email', 'password','department','depart')
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
    
class RescheduleSerializer(serializers.ModelSerializer):
    visiting_to = serializers.CharField(source='visiting_to.username')
    class Meta:
        model = Visitor
        fields = ['id','meeting_date', 'meeting_time','status','visiting_to']
        read_only_fields = ['id','visiting_to']
        # read_only_fields = ['id','name','email','photo','visiting_to','reason','department']

    # def validate(self, data):
    #     allowed_fields = {'meeting_date', 'meeting_time'}
    #     invalid_fields = set(data.keys()) - allowed_fields

    #     if invalid_fields:
    #         raise serializers.ValidationError(
    #             {field: "This field cannot be modified." for field in invalid_fields}
    #         )
    #     return data

    # def update(self, instance, validated_data):
    #     instance.meeting_date = validated_data.get('meeting_date', instance.meeting_date)
    #     instance.meeting_time = validated_data.get('meeting_time', instance.meeting_time)
    #     instance.save()
    #     return instance