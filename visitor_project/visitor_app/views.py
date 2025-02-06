from django.shortcuts import render
from .models import CustomUser, Department, Visitor
from .serializers import UserSerializer, LoginSerializer, VisitorSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView

# Create your views here.
class UserRegistrationView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'status': 'success','message': 'User created successfully.','data': UserSerializer(user).data}, status=status.HTTP_201_CREATED)
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
                    'user': UserSerializer(user).data
                }
            }, status=status.HTTP_200_OK)
        
        return Response({
            'status': 'error',
            'message': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    
class RegisterVisiterView(APIView):
    serializer_class = VisitorSerializer
    def post(self, request, pk=None):
        serializer = VisitorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Meeting Appointed'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VisitorView(ListAPIView):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer