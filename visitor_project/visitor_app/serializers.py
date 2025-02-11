from rest_framework import serializers
from .models import Visitor
from host_app.models import Department

class VisitorSerializer(serializers.ModelSerializer):
    department = serializers.CharField(source='visiting_to.department.name', read_only=True)
    # department = serializers.CharField(source='visiting_to.department.name')
    # department = serializers.PrimaryKeyRelatedField(source='visiting_to.department.name',queryset=Department.objects.all(), required=True)

    visiting_to = serializers.CharField(source='visiting_to.username', read_only=True)
    host = serializers.CharField(source='visiting_to.username', read_only=True)
    class Meta:
        model = Visitor
        # fields = '__all__'
        fields = ['id','name', 'email','photo','status','visiting_to', 'meeting_date', 'meeting_time','reason', 'department','host']
        read_only_fields = ['status']
