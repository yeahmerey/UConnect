from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated , AllowAny
from .serializers import RegisterSerializer 
from rest_framework import status
class LogoutView(APIView) : 
    permission_classes = [IsAuthenticated]

    def post(self , request) : 
        return Response({"message": "Succesfully logged out."})

class RegisterView(APIView):
    permission_classes = [AllowAny]    

    def post(self , request):
        serialzier = RegisterSerializer(data=request.data)
        if serialzier.is_valid():
            serialzier.save()
            return Response({"message": "User registered successfully"})
        return Response(serialzier.errors , status=status.HTTP_400_BAD_REQUEST)
    