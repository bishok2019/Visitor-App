from django.shortcuts import render,get_object_or_404
from .models import Host
from visitor_app.models import Visitor
from visitor_app.serializers import VisitorSerializer
from .serializers import HostSerializer, LoginSerializer, DepartmentSerializer, RescheduleSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Create your views here.
class DepartmentRegistrationView(APIView):
    permission_classes = [IsAdminUser]
    serializer_class = DepartmentSerializer
    
    def post(self, request):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            department = serializer.save()
            return Response({'status': 'success','message': 'Department created successfully.','data': DepartmentSerializer(department).data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HostRegistrationView(APIView):
    permission_classes = [AllowAny]
    serializer_class = HostSerializer
    
    def post(self, request):
        serializer = HostSerializer(data=request.data)
        if serializer.is_valid():
            host = serializer.save()
            return Response({'status': 'success','message': 'Host created successfully.','data': HostSerializer(host).data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class HostLoginView(APIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = LoginSerializer(data=request.data,context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            
            return Response({
                'status': 'success',
                'message': 'Login successful',
                'data': {
                    'user': HostSerializer(user).data
                }
            }, status=status.HTTP_200_OK)
        
        return Response({
            'status': 'error',
            'message': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    
class ModifyHostView(APIView):
    permission_classes = [IsAdminUser]
    serializer_class = HostSerializer    
    def get(self, request, pk=None, format=None):
        host = Host.objects.filter(pk=pk)
        if not host.exists():
            return Response({"msg": "Host not found."}, status=status.HTTP_404_NOT_FOUND)
        host = host.first()
        serializer = HostSerializer(host)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def patch(self, request, pk=None, format=None):
        host = Host.objects.filter(pk=pk)
        if not host.exists:
            return Response({"msg":"Host Deosnot exist!"}, status=status.HTTP_404_NOT_FOUND)
        host = host.first()
        serializer = HostSerializer(host, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Partial Data Updated !!"})
    
    def delete(self, request, pk=None, format=None):
        host = Host.objects.filter(pk=pk)
        if not host.exists:
            return Response({"msg":"Host Deosnot exist!"}, status=status.HTTP_404_NOT_FOUND)
        host = host.first()
        host.delete()
        return Response({'msg': 'Data Deleted!'}, status=status.HTTP_204_NO_CONTENT)
    
class ListHostView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Host.objects.all()
    serializer_class = HostSerializer

class YourAppointmentView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = VisitorSerializer
    def get(self, request):
        host = request.user
        visitors = Visitor.objects.filter(visiting_to=host)

        if visitors.exists():
            serializer = VisitorSerializer(visitors, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"msg":"You have no appointment for now!"}, status=status.HTTP_404_NOT_FOUND)

class GetYourHostInfo(APIView):
    permission_classes=[IsAuthenticated]
    serializer_class = HostSerializer
    def get(self, request):
        host= request.user
        serializer = HostSerializer(host)
        return Response(serializer.data)
            
class RescheduleVisitor(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RescheduleSerializer    

    def get(self, request,pk=None):
        host = request.user
        visitors = Visitor.objects.filter(pk=pk, visiting_to=host)

        if visitors.exists():
            serializer = RescheduleSerializer(visitors, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"msg": "Appointment not found."}, status=status.HTTP_404_NOT_FOUND)
    
    def patch(self, request, pk=None, format=None):
        host = request.user
        visitor = Visitor.objects.filter(pk=pk, visiting_to=host).first()
        if not visitor:
            return Response({"msg": "Appointment not found."},status=status.HTTP_404_NOT_FOUND)
        if visitor.visiting_to!=host:
            return Response(
                {"msg": "You do not have permission to reschedule this appointment."},status=status.HTTP_403_FORBIDDEN)
        serializer = RescheduleSerializer(visitor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Appointment successfully rescheduled!'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk=None, format=None):
        host = request.user
        visitor = Visitor.objects.filter(pk=pk,visiting_to=host)
        if not visitor:
            return Response({"msg": "Appointment not found."},status=status.HTTP_404_NOT_FOUND)
        if visitor.visiting_to != request.user:
            return Response({"msg": "You do not have permission to delete this appointment."},status=status.HTTP_403_FORBIDDEN)
        visitor.delete()
        return Response({'msg': 'Appointment successfully deleted!'}, status=status.HTTP_204_NO_CONTENT)