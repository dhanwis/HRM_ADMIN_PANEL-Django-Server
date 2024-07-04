from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import status
from .serializers import *
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate,login
from .models import *
from rest_framework.authentication import TokenAuthentication
from rest_framework import  permissions

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

            serializer.save(is_teamlead = True,role='teamlead')
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
            serializer.save(is_staff = True,role='staff')
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
            serializer.save(is_frontoffice = True,role='frontoffice')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  

########################################################### HR #############################################################  
    
class HRListCreate(APIView):
    def get(self, request, format=None):
        hr = User.objects.filter(is_hr = True)
        serializer = UserSerializer(hr, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():   
            serializer.save(is_hr = True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


################################################################# intern ###################################################

    

class InternCreateView(APIView):
    def get(self, request, format=None):
        hr = User.objects.filter(is_intern = True)
        serializer = UserInternSerializer(hr, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
    def post(self, request, *args, **kwargs):
        serializer = UserInternSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            response_data = {
                'message': 'Intern registered successfully.',
                'user': serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

class InternLoginView(APIView) :
    def post(self, request) :
        data=request.data
        username = data.get('username')
        password = data.get('password')

        intern = authenticate(username=username, password=password)
        if intern and intern.is_intern == True:
            serializer = UserInternSerializer(intern)
            token, created = Token.objects.get_or_create(user=intern)
            return Response({"user":serializer.data,"token":token.key},status=status.HTTP_200_OK)
        return Response({"details":"invalid credentials"},status=status.HTTP_400_BAD_REQUEST)

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
    


class ReferencelistCreate(APIView):
    def get(self, request, format=None):
        reference=Reference.objects.all()
        serializer= ReferenceSerializer(reference,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = ReferenceSerializer(data=request.data)
        if serializer.is_valid():   
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ReferenceUpdate(APIView):
    def get(self,request,reference_id,format=None):
        reference=Reference.objects.get(id=reference_id)
        serializer=ReferenceSerializer(reference )
        return Response(serializer.data,status=status.HTTP_200_OK)
    def patch(self,request,reference_id,format=None):
        reference=Reference.objects.get(id=reference_id)
        serializer=ReferenceSerializer(reference,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
############################################    Fee    ############################################################################

# class FeelistCreate(APIView):
#     def get(self, request, format=None):
#         fee=Fee.objects.all()
#         serializer= FeedbackSerializer(fee,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
    
##################################################Feedback#####################################################################

class FeedbackListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def get(self, request, format=None):
        feedback = Feedback.objects.all()
        serializer = FeedbackSerializer(feedback, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
    def post(self, request, format=None):
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():   
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#####################################################Testimonial##################################################################

class TestimonialListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def get(self, request, format=None):
        testimonial = testimonial.objects.all()
        serializer = TestimonialSerializer(testimonial, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
    def post(self, request, format=None):
        serializer = TestimonialSerializer(data=request.data)
        if serializer.is_valid():   
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

