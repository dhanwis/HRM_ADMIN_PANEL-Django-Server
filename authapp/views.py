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
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
import razorpay
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
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
            serializer.save(is_teamlead = True,role='Teamlead')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

 ###################################################### staff ############################################################### 
    
class StaffListCreate(APIView):
    def get(self, request, format=None):
        staff = User.objects.filter(is_staff = True,is_superuser=False)
        serializer = UserSerializer(staff, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():   
            serializer.save(is_staff = True,role='Staff')
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
            serializer.save(is_frontoffice = True,role='Frontoffice')
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
        intern = User.objects.filter(is_intern = True)
        serializer = UserInternSerializer(intern, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
    def post(self, request, *args, **kwargs):
        serializer = UserInternSerializer(data=request.data)
        print(request.data)     
        if serializer.is_valid():
            user = serializer.save(is_intern = True,role="intern")
          
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
    
class ReferenceDelete(APIView):
    def get(self,request,reference_id,format=None):
        reference=Reference.objects.get(id=reference_id)
        serializer=ReferenceSerializer(reference )
        return Response(serializer.data,status=status.HTTP_200_OK)
    def delete(self,request,reference_id,format=None):
        try:
            reference=Reference.objects.get(id=reference_id)
            reference.delete()
            return Response({"message":"table deleted successfully"},status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"error":" table not found"},status=status.HTTP_404_NOT_FOUND)
        
    ##################################################################################################################

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
            serializer.save(user=request.user)
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


class    Allusers(APIView):
    def get(self, request, format=None):
        user= User.objects.filter(is_hr= False,is_superuser=False,is_intern=False )
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def delete(self, request, pk, format=None):
        user = get_object_or_404(User, pk=pk, is_hr=False, is_superuser=False, is_intern=False)
        user.delete()
        return Response(status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        user = get_object_or_404(User, pk=pk, is_hr=False, is_superuser=False, is_intern=False)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class LoginAll(APIView):
    def post(self, request, format=None):
        data = request.data
        username = data.get('username')
        password = data.get('password')

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user:
            # Create or retrieve token for authenticated user
            serializer = UserSerializer(user)
            token, created = Token.objects.get_or_create(user=user)
            
            # Determine the role and add role information to the response
            if user.is_hr:
                role = "HR"
            elif user.is_teamlead:
                role = "Teamlead"
            elif user.is_staff:
                role = "Staff"
            elif user.is_frontoffice:
                role = "Frontoffice"
            else:
                role = "Unknown"  # Fallback in case no role is identified

            # Return user details, role, and token
            return Response({
                "user": serializer.data,
                "role": role,
                "token": token.key
            }, status=status.HTTP_200_OK)

        return Response({"details": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
    
    
class EmployeeCountAPIView(APIView):
    def get(self, request, format=None):
        # Filter out users who are HR or interns
        employee_count = User.objects.filter(is_hr=False, is_intern=False,is_superuser=False).count()

        # Return the total count of employees
        return Response({
            "employee_count": employee_count
        }, status=status.HTTP_200_OK)
        
class InternCount(APIView):
    def get(self,request,fromat=None):
        intern_count=User.objects.filter(is_intern=True).count()
        return Response({"interncount":intern_count},status=status.HTTP_200_OK)
    
    

razorpay_client = razorpay.Client(auth=("rzp_test_y6JLI3UpfjyFVW", "mlQr9hUdx6k9xmbPNQS0IWD3"))

class CreateOrderView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            amount = request.data.get('amount')  # Amount in paise (e.g., Rs. 500 => 50000)
            currency = "INR"

            # Create Razorpay order
            payment_order = razorpay_client.order.create({
                "amount": amount,
                "currency": currency,
                "payment_capture": 1  # Auto-capture after payment
            })

            return Response({
                'order_id': payment_order['id'],
                'amount': payment_order['amount'],
                'currency': payment_order['currency']
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['POST'])
def verify_payment(request):
    try:
        data = request.data
        razorpay_client.utility.verify_payment_signature({
            'razorpay_order_id': data['razorpay_order_id'],
            'razorpay_payment_id': data['razorpay_payment_id'],
            'razorpay_signature': data['razorpay_signature']
        })
        return Response({'message': 'Payment verified successfully.'}, status=status.HTTP_200_OK)
    except razorpay.errors.SignatureVerificationError:
        return Response({'error': 'Payment verification failed.'}, status=status.HTTP_400_BAD_REQUEST)
    
