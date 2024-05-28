from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import status
from .serializers import *

# Create your views here.

############################################### team lead ############################################################## 
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
    
    
 ###################################################### staff ############################################################### 
    
class StaffListCreate(APIView):
    def get(self, request, format=None):
        staff = User.objects.filter(is_staff = True)
        serializer = UserSerializer(staff, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():   
            serializer.save(is_staff = True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
 
 ########################################################## front office ################################################   
class FrontOfficeListCreate(APIView):
    def get(self, request, format=None):
        frontoffice = User.objects.filter(is_frontoffice = True)
        serializer = UserSerializer(frontoffice, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():   
            serializer.save(is_frontoffice = True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
########################################################### HR #############################################################  
    
class HRListCreate(APIView):
    def get(self, request, format=None):
        hr = User.objects.filter(is_admin = True)
        serializer = UserSerializer(hr, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():   
            serializer.save(is_admin = True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


################################################################# intern ###################################################

class InternListCreate(APIView):
    def get(self, request, format=None):
        intern = User.objects.filter(is_intern = True)
        serializer = UserSerializer(intern, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():   
            serializer.save(is_intern = True)
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