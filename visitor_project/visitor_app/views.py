from .models import Visitor
from .serializers import VisitorSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser, AllowAny

# Create your views here.
class RegisterVisitorView(APIView):
    serializer_class = VisitorSerializer
    permission_classes = [AllowAny]
    def post(self, request, pk=None):
        serializer = VisitorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Meeting Appointed'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VisitorView(ListAPIView):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer
    permission_classes = [IsAdminUser]

# class ModifyVisitorView(APIView):
#     permission_classes = [IsAdminUser]
#     serializer_class = VisitorSerializer

#     def get(self, request, pk=None):
#         visitors = Visitor.objects.filter(pk=pk)
#         if not visitors.exists():
#             return Response({"msg": "Visitor not found."}, status=status.HTTP_404_NOT_FOUND)
#         visitor = visitors.first()
#         serializer = VisitorSerializer(visitor)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def patch(self, request, pk=None, format=None):
#         visitors = Visitor.objects.filter(pk=pk)
#         if not visitors.exists():
#             return Response({"msg": "Visitor Does not Exist!"}, status=status.HTTP_404_NOT_FOUND)
#         visitor = visitors.first()
#         serializer = VisitorSerializer(visitor, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Partial Data Updated!'}, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
#     def delete(self, request, pk=None, format=None):
#         visitors = Visitor.objects.filter(pk=pk)
#         if not visitors.exists():
#             return Response({"msg": "Visitor does not exist!"}, status=status.HTTP_404_NOT_FOUND)
#         visitor = visitors.first()
#         visitor.delete()
#         return Response({'msg': 'Data Deleted!'}, status=status.HTTP_204_NO_CONTENT)