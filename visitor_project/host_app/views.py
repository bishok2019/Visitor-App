from django.shortcuts import render
from .models import Host, Department
from .serializers import HostSerializer, LoginSerializer, DepartmentSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

# Create your views here.
class DepartmentRegistrationView(APIView):
    permission_classes = [AllowAny]
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
    
class LoginView(APIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
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
    # permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = HostSerializer    
    def get(self, request, pk=None, format=None):
        id=pk
        if id is not None:
            try:
                host=Host.objects.get(id=id)
                serializer = HostSerializer(host)
                return Response(serializer.data)
            except Host.DoesNotExist:
                return Response({"msg":"Host doesnot exist!"}, status=status.HTTP_404_NOT_FOUND)
                    
        host = Host.objects.all()
        serializer = HostSerializer(host, many=True)
        return Response(serializer.data)
    
    def patch(self, request, pk=None, format=None):
        id=pk
        try:
            host = Host.objects.get(pk=id)
        except Host.DoesNotExist:
            return Response({"msg":"Host Does not Exist!"}, status=status.HTTP_404_NOT_FOUND)
            
        serializer = HostSerializer(host, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated!'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None, format=None):
        id=pk
        try:
            host = Host.objects.get(pk=id)
        except Host.DoesNotExist:
            return Response({"msg":"host Does not Exist!"}, status=status.HTTP_404_NOT_FOUND)
            
        serializer = HostSerializer(host, data=request.data,)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated!'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk=None, format=None):
        id=pk
        try:
            host = Host.objects.get(pk=id)
            host.delete()
            return Response({'msg':'Data Deleted!'})
        except Host.DoesNotExist:
            return Response({"msg":"Host doesnot exist!"}, status=status.HTTP_404_NOT_FOUND)