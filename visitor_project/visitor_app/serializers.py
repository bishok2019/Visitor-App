from rest_framework import serializers
from .models import Visitor
from host_app.models import Department

# class VisitorSerializer(serializers.ModelSerializer):
#     department = serializers.CharField(source='visiting_to.department.name', read_only=True)
#     # visiting_to = serializers.CharField(source='visiting_to.username')
#     host = serializers.CharField(source='visiting_to.username', read_only=True)
#     class Meta:
#         model = Visitor
#         # fields = '__all__'
#         fields = ['id','name', 'email','photo','status','visiting_to', 'meeting_date', 'meeting_time','reason','host','department',]
#         read_only_fields = ['status']

class VisitorSerializer(serializers.ModelSerializer):
    department = serializers.CharField(source='visiting_to.department.name', read_only=True)
    class Meta:
        model = Visitor
        fields = ['id','name', 'email','photo','phone_num','status','visiting_to', 'meeting_date', 'meeting_time','reason','department',]
        read_only_fields = ['status']

class VisitorInfoSerializer(serializers.ModelSerializer):
    department = serializers.CharField(source='visiting_to.department.name', read_only=True)
    visiting_to = serializers.CharField(source='visiting_to.username', read_only=True)

    class Meta:
        model = Visitor
        fields = ['id','name', 'email','photo','phone_num','status','visiting_to', 'meeting_date', 'meeting_time','reason','department',]
        read_only_fields = ['status']