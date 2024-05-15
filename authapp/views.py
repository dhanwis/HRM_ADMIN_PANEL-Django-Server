from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import status
from .serializers import *

# Create your views here.

  
class TeamLeadListCreate(APIView):
    def get(self, request, format=None):
        team_lead = User.objects.filter(is_teamlead = True)
        serializer = UserSerializer(team_lead, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():   
            serializer.save(is_teamlead = True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
{
    "username": "Devika",
    "password":"password",
    
    "first_name": "hh",
    "last_name": "devika",
    "email": "devikamanayil@gmail.com",  
    "phone": "09632154845",
    "address": "rose villa"
}