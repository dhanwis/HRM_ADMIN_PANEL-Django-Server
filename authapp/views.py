from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import status
from .serializers import UserSerializer
from .models import User
from django.contrib.auth import authenticate,login
from rest_framework.authtoken.models import Token
# Team Lead View

################################################# team lead ###########################################################################
class TeamLeadListCreate(APIView):
    """
    API endpoint for listing and creating Team Leads.
    """
    def get(self, request, format=None):
        """
        Get a list of all Team Leads.
        """
        team_leads = User.objects.filter(is_teamlead=True)
        serializer = UserSerializer(team_leads, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request, format=None):
        """
        Create a new Team Lead.
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():   
            serializer.save(is_teamlead=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
#team login

   
class TeamLogin(APIView):
    def post(self,request,format=None):
        data=request.data
        username=data.get('username')
        password=data.get('password')
        
        teamlead=authenticate(request,username=username,password=password)
        if teamlead and teamlead.is_teamlead:
            serializer=UserSerializer(teamlead)
            token,created=Token.objects.get_or_create(user=teamlead)
            return Response({"user":serializer.data,"token":token.key},status=status.HTTP_200_OK)
        return Response({"details":"invalid credentials"},status=status.HTTP_400_BAD_REQUEST)

# Staff View

########################################################################### staff ####################################################
class StaffListCreate(APIView):
    """
    API endpoint for listing and creating Staff members.
    """
    def get(self, request, format=None):
        """
        Get a list of all Staff members.
        """
        staff = User.objects.filter(is_staff=True)
        serializer = UserSerializer(staff, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request, format=None):
        """
        Create a new Staff member.
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():   
            serializer.save(is_staff=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    
#staff login   
class StaffLogin(APIView):
    def post(self,request,format=None):
        data=request.data
        username=data.get('username')
        password=data.get('password')
        
        staff=authenticate(request,username=username,password=password)
        if staff and staff.is_staff:
            serializer=UserSerializer(staff)
            token,created=Token.objects.get_or_create(user=staff)
            return Response({"user":serializer.data,"token":token.key},status=status.HTTP_200_OK)
        return Response({"details":"invalid credentials"},status=status.HTTP_400_BAD_REQUEST)

# Front Office View

################################################## front office ####################################################################
class FrontOfficeListCreate(APIView):
    """
    API endpoint for listing and creating Front Office members.
    """
    def get(self, request, format=None):
        """
        Get a list of all Front Office members.
        """
        front_office = User.objects.filter(is_frontoffice=True)
        serializer = UserSerializer(front_office, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request, format=None):
        """
        Create a new Front Office member.
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():   
            serializer.save(is_frontoffice=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#front login   
class FrontLogin(APIView):
    def post(self,request,format=None):
        data=request.data
        username=data.get('username')
        password=data.get('password')
        
        frontoffice=authenticate(request,username=username,password=password)
        if frontoffice and frontoffice.is_frontoffice:
            serializer=UserSerializer(frontoffice)
            token,created=Token.objects.get_or_create(user=frontoffice)
            return Response({"user":serializer.data,"token":token.key},status=status.HTTP_200_OK)
        return Response({"details":"invalid credentials"},status=status.HTTP_400_BAD_REQUEST)    
    
    
####################################################### HR #############################################################################

#hr login 
class Login(APIView):
    def post(self,request,format=None):
        data=request.data
        username=data.get('username')
        password=data.get('password')
        
        hr=authenticate(request,username=username,password=password)
        if hr and hr.is_hr:
            serializer=UserSerializer(hr)
            token,created=Token.objects.get_or_create(user=hr)
            return Response({"user":serializer.data,"token":token.key},status=status.HTTP_200_OK)
        return Response({"details":"invalid credentials"},status=status.HTTP_400_BAD_REQUEST)
# HR View
class HRListCreate(APIView):
    """
    API endpoint for listing and creating HR members.
    """
    def get(self, request, format=None):
        """
        Get a list of all HR members.
        """
        hr = User.objects.filter(is_hr=True)
        serializer = UserSerializer(hr, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request, format=None):
        """
        Create a new HR member.
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():   
            serializer.save(is_hr=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
########################################################## intern #######################################################################
# Intern View
class InternListCreate(APIView):
    """
    API endpoint for listing and creating Interns.
    """
    def get(self, request, format=None):
        """
        Get a list of all Interns.
        """
        interns = User.objects.filter(is_intern=True)
        serializer = UserSerializer(interns, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request, format=None):
        """
        Create a new Intern.
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():   
            serializer.save(is_intern=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#intern login 
class InternLogin(APIView):
    def post(self,request,format=None):
        data=request.data
        username=data.get('username')
        password=data.get('password')
        
        intern=authenticate(request,username=username,password=password)
        if intern and intern.is_intern:
            serializer=UserSerializer(intern)
            token,created=Token.objects.get_or_create(user=intern)
            return Response({"user":serializer.data,"token":token.key},status=status.HTTP_200_OK)
        return Response({"details":"invalid credentials"},status=status.HTTP_400_BAD_REQUEST)


#############################################################################################################################################
    
{
    "username": "Devika",
    "password":"password",
    
    "first_name": "hh",
    "last_name": "devika",
    "email": "devikamanayil@gmail.com",  
    "phone": "09632154845",
    "address": "rose villa"
}

class Login(APIView):
    def post(self,request,format=None):
        data=request.data
        username=data.get('username')
        password=data.get('password')
        
        hr=authenticate(request,username=username,password=password)
        if hr and hr.is_hr==True:
            serializer=UserSerializer(hr)
            token,created=Token.objects.get_or_create(user=hr)
            return Response({"user":serializer.data,"token":token.key},status=status.HTTP_200_OK)
        return Response({"details":"invalid credentials"},status=status.HTTP_400_BAD_REQUEST)
    
    
    
class LoginTeamlead(APIView):
    def post(self,request,format=None):
        data=request.data
        username=data.get('username')
        password=data.get('password')
        
        teamlead=authenticate(request,username=username,password=password)
        if teamlead and teamlead.is_teamlead==True:
            serializer=UserSerializer(teamlead)
            token,created=Token.objects.get_or_create(user=teamlead)
            return Response({"user":serializer.data,"token":token.key},status=status.HTTP_200_OK)
        return Response({"details":"invalid credentials"},status=status.HTTP_400_BAD_REQUEST)
    
    
    
class LoginStaff(APIView):
    def post(self,request,format=None):
        data=request.data
        username=data.get('username')
        password=data.get('password')
        
        staff=authenticate(request,username=username,password=password)
        if staff and staff.is_staff==True:
            serializer=UserSerializer(staff)
            token,created=Token.objects.get_or_create(user=staff)
            return Response({"user":serializer.data,"token":token.key},status=status.HTTP_200_OK)
        return Response({"details":"invalid credentials"},status=status.HTTP_400_BAD_REQUEST)
    
    

class LoginFrontoffice(APIView):
    def post(self,request,format=None):
        data=request.data
        username=data.get('username')
        password=data.get('password')
        
        frontoffice=authenticate(request,username=username,password=password)
        if frontoffice and frontoffice.is_frontoffice==True:
            serializer=UserSerializer(frontoffice)
            token,created=Token.objects.get_or_create(user=frontoffice)
            return Response({"user":serializer.data,"token":token.key},status=status.HTTP_200_OK)
        return Response({"details":"invalid credentials"},status=status.HTTP_400_BAD_REQUEST)
    
    

class LoginIntern(APIView):
    def post(self,request,format=None):
        data=request.data
        username=data.get('username')
        password=data.get('password')
        
        intern=authenticate(request,username=username,password=password)
        if intern and intern.is_intern==True:
            serializer=UserSerializer(intern)
            token,created=Token.objects.get_or_create(user=intern)
            return Response({"user":serializer.data,"token":token.key},status=status.HTTP_200_OK)
        return Response({"details":"invalid credentials"},status=status.HTTP_400_BAD_REQUEST)
