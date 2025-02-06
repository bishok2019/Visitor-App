from rest_framework import serializers
from .models import Visitor

class VisitorSerializer(serializers.ModelSerializer):
    department = serializers.CharField(source='visiting_to.department.name', read_only=True)
    host = serializers.CharField(source='visiting_to.username', read_only=True)
    class Meta:
        model = Visitor
        # fields = '__all__'
        fields = ['name', 'visiting_to', 'meeting_date', 'meeting_time','reason', 'created_at', 'department','host']