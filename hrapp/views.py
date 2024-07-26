from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import status,viewsets
from .serializers import *
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics, permissions
from rest_framework.authentication import TokenAuthentication

# Create your views here.
class TeamLeadAssignCreate(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def get(self, request, format=None):
        team_lead = TeamleadAssign.objects.filter(user=request.user)
        serializer = TeamLeadAssignSerializer(team_lead, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
            
    def post(self, request, format=None):
        serializer = TeamLeadAssignSerializer(data=request.data)
        if serializer.is_valid():   
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TeamLeadAssignhr(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def get(self, request, format=None):
        team_lead = TeamleadAssign.objects.all()
        serializer = TeamLeadAssignSerializer(team_lead, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)    
    
class TeamLeadAssignUpdate(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def get(self,request,teamlead_id,format=None):
        team=TeamleadAssign.objects.get(id=teamlead_id)
        serializer=TeamLeadAssignSerializer(team )
        return Response(serializer.data,status=status.HTTP_200_OK)
    def patch(self,request,teamlead_id,format=None):
        team=TeamleadAssign.objects.get(id=teamlead_id)
        serializer=TeamLeadAssignSerializer(team,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    
    
    
#############################DELETE####################

class TeamLeadAssignDelete(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes=[TokenAuthentication]

    def get(self,request,teamlead_id,format=None):
        try:
            team_lead=TeamleadAssign.objects.get(id=teamlead_id)
            serializer=TeamLeadAssignSerializer(team_lead)
            return Response(serializer.data,status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"error":"teamlead not found"},status=status.HTTP_404_NOT_FOUND)
    def delete(self,request,teamlead_id,format=None):
        try:
            team_lead=TeamleadAssign.objects.get(id=teamlead_id)
            team_lead.delete()
            return Response({"message":"Teamlead deleted succesfully"},status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"error":"Teamlead not found"},status=status.HTTP_404_NOT_FOUND)

class StudentAssignlistCreate(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def get(self, request, format=None):
        student_assign=StudentAssign.objects.all()
        serializer= StudentAssignSerializer(student_assign,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        print(request.data)
        serializer = StudentAssignSerializer(data=request.data)
        if serializer.is_valid():   
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class StudentStatusUpdateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def patch(self, request, pk):
        try:
            student_assign = StudentAssign.objects.get(pk=pk)
        except StudentAssign.DoesNotExist:
            return Response({"error": "StudentAssign not found"}, status=status.HTTP_404_NOT_FOUND)
        
        if student_assign.status == 'Completed':
            return Response({"error": "Cannot modify a completed task"}, status=status.HTTP_400_BAD_REQUEST)
        
        action = request.data.get('action')
        
        if action == 'start':
            student_assign.status = 'In progress'
        elif action == 'end':
            student_assign.status = 'Completed'
        else:
            return Response({"error": "Invalid action"}, status=status.HTTP_400_BAD_REQUEST)
        
        student_assign.save()
        serializer = StudentStatusUpdateSerializer(student_assign)
        return Response(serializer.data)

class StudentAssignDelete(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def get(self,request,student_id,format=None):
        try:
            student_assign=StudentAssign.objects.get(id=student_id)
            serializer=StudentAssignSerializer(student_assign)
            return Response(serializer.data,status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"error":"student not found"},status=status.HTTP_404_NOT_FOUND)
    def delete(self,request,student_id,format=None):
        try:
            student_task=StudentAssign.objects.get(id=student_id)
            student_task.delete()
            return Response({"message":"student task deleted succesfully"},status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"error":"Teamlead not found"},status=status.HTTP_404_NOT_FOUND)
    

class AssignProjectCreate(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def get(self, request, format=None):
        project_assign=AssignProject.objects.filter(employeename=request.user)
        serializer=AssignProjectSerializer(project_assign,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = AssignProjectSerializer(data=request.data)
        if serializer.is_valid():   
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    
    
class AssignProjectStatusUpdate(APIView) :
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def patch(self, request, pk) :
        try :
            project_assign = AssignProject.objects.get(pk=pk)
        except AssignProject.DoesNotExist:
            return Response({"error" : "project assign not found"}, status=status.HTTP_404_NOT_FOUND)
        
        if project_assign.status == 'Completed' :
            return Response({"error" : "Cannot modify the completed task"})
        
        action = request.data.get('action')

        if action == 'start' :
            project_assign.status = 'In progress'
        elif action == 'end' :
            project_assign.status = 'Completed'
        else :
            return Response({"error": "Invalid action"}, status=status.HTTP_400_BAD_REQUEST)
        
        project_assign.save()
        serializer = AssignProjectUpdateSerializer(project_assign)
        return Response(serializer.data)
    def delete(self, request, pk):
        try:
            project_assign = AssignProject.objects.get(pk=pk)
        except AssignProject.DoesNotExist:
            return Response({"error": "project assign not found"}, status=status.HTTP_204_NO_CONTENT)

        project_assign.delete()
        return Response({"message": "Project assignment deleted successfully"}, status=status.HTTP_200_OK)



# class Process_Leave_Request(APIView):

#      def process_leave_request(request, request_id):
      
#       try:

#         leave_request = LeaveRequest.objects.get(pk=request_id)
#       except LeaveRequest.DoesNotExist:
#         return Response({'message': 'Leave request not found'}, status=status.HTTP_404_NOT_FOUND)

#       action = request.data.get('action')

#       if action not in ['accept', 'reject']:
#         return Response({'message': 'Invalid action'}, status=status.HTTP_400_BAD_REQUEST)

#       leave_request.status = 'accepted' if action == 'accept' else 'rejected'
#       leave_request.save()

#       serializer = LeaveRequestSerializer(leave_request)
#       return Response({'message': f'Leave request {action}ed successfully', 'leave_request': serializer.data}, status=status.HTTP_200_OK)


class LeaveLetterCreate(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def get(self, request):
        leaves = Leave.objects.filter(name=request.user)
        serializer = LeaveSerializer(leaves, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LeaveSerializer(data=request.data, context={'request': request})
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def get_queryset(self):
        return self.queryset.filter(name=self.request.user)
   

class LeaveListView(generics.ListAPIView):
    queryset = Leave.objects.all()
    serializer_class = LeaveListSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes=[TokenAuthentication]

class LeaveUpdateView(generics.UpdateAPIView):
    queryset = Leave.objects.all()
    serializer_class = LeaveUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes=[TokenAuthentication]

    def get_queryset(self):
        return self.queryset.filter(status='Pending')
    


class NotesSharinglistCreate(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def get(self, request, format=None):
        notes=Noteupload.objects.filter(student_name=request.user)
        serializer= NotesSharingSerializer(notes,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = NotesSharingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StatusSharinglistCreate(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def get(self, request, format=None):
        statusshare=StatusShare.objects.filter(Teamleadname=request.user)
        serializer= StatusShareSerializer(statusshare,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = StatusShareSerializer(data=request.data)
        if serializer.is_valid():   
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

########################## digital marketing table create ###################################################################################

class DigitalTableCreate(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def get(self, request, format=None):
        digital_table=DigitalTable.objects.all()
        serializer= DigitalTableSerializer(digital_table,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = DigitalTableSerializer(data=request.data)
        if serializer.is_valid():   
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    
################### digital marketing table update ##########################################################################################


class DigitalTableUpdate(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def get(self,request,digital_id,format=None):
        digtaltable=DigitalTable.objects.get(id=digital_id)
        serializer=DigitalTableSerializer(digtaltable)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def patch(self,request,digital_id,format=None):
        digtaltable=DigitalTable.objects.get(id=digital_id)
        serializer=DigitalTableSerializer(digtaltable,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
    
####################################### digital marketing table deletion #################################################################


class DigitalTableDelete(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def get(self,request,digital_id,format=None):
        try:
            digitaltable=DigitalTable.objects.get(id=digital_id)
            serializer=DigitalTableSerializer(digitaltable)
            return Response(serializer.data,status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"error":"table  not found"},status=status.HTTP_404_NOT_FOUND)
    def delete(self,request,digital_id,format=None):
        try:
            digitaltable=DigitalTable.objects.get(id=digital_id)
            digitaltable.delete()
            return Response({"message":"table deleted successfully"},status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"error":" table not found"},status=status.HTTP_404_NOT_FOUND)
        
class JobApplyCreate(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def get(self, request, format=None):
        job_apply=JobApply.objects.all()
        serializer= JobApplySerializer(job_apply,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = JobApplySerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():   
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,job_id,format=None):
        try:
            job_apply=JobApply.objects.get(id=job_id)
            job_apply.delete()
            return Response({"message":"table deleted successfully"},status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"error":" table not found"},status=status.HTTP_404_NOT_FOUND)

class CallsheetCreate(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def get(self, request, format=None):
        call_sheet=callsheet.objects.all()
        serializer= CallsheetSerializer(call_sheet,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = CallsheetSerializer(data=request.data)
        if serializer.is_valid():   
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


############################################################### callsheet creation ################################################


class CallsheetCreate(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def get(self, request, format=None):
        call_sheet=callsheet.objects.all()
        serializer= CallsheetSerializer(call_sheet,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = CallsheetSerializer(data=request.data)
        if serializer.is_valid():   
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
############################################################### callsheet update ####################################################

class CallsheetUpdate(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def get(self,request,callsheet_id,format=None):
        call_sheet=callsheet.objects.get(id=callsheet_id)
        serializer=CallsheetSerializer(call_sheet)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def patch(self,request,callsheet_id,format=None):
        call_sheet=callsheet.objects.get(id=callsheet_id)
        serializer=CallsheetSerializer(call_sheet,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
############################################################### callsheet delete #################################################

class CallsheetDelete(APIView):
    def get(self,request,callsheet_id,format=None):
        try:
           call_sheet=callsheet.objects.get(id=callsheet_id)
           serializer=CallsheetSerializer(call_sheet)
           return Response(serializer.data,status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"error":"Project not found"},status=status.HTTP_404_NOT_FOUND)
    def delete(self,request,callsheet_id,format=None):
        try:
            call_sheet=callsheet.objects.get(id=callsheet_id)
            call_sheet.delete()
            return Response({"message":"Project deleted successfully"},status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist:
            return Response({"error":"Project not found"},status=status.HTTP_404_NOT_FOUND)

################################################################ quatation creatation ##############################################

class QuatationCreate(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def get(self, request, format=None):
        quatation_create=quotation.objects.all()
        serializer= QuatationSerializer(quatation_create,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = QuatationSerializer(data=request.data)
        if serializer.is_valid():   
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
################# quatation update ############


class QuatationUpdate(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def get(self,request,quatation_id,format=None):
        quatation_update=quotation.objects.get(id=quatation_id)
        serializer=QuatationSerializer(quatation_update)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def patch(self,request,quatation_id,format=None):
        quatation_update=quotation.objects.get(id=quatation_id)
        serializer=QuatationSerializer(quatation_update,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
 ######################quatation delete ####################

class QuatationDelete(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def get(self,request,quatation_id,format=None):
        try:
           quatation_delete=quotation.objects.get(id=quatation_id)
           serializer=QuatationSerializer(quatation_delete)
           return Response(serializer.data,status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"error":"Project not found"},status=status.HTTP_404_NOT_FOUND)
    def delete(self,request,quatation_id,format=None):
        try:
            quotation_delete=quotation.objects.get(id=quatation_id)
            quotation_delete.delete()
            return Response({"message":"Project deleted successfully"},status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"error":"Project not found"},status=status.HTTP_404_NOT_FOUND)

class MachineAllocateViewSet(viewsets.ModelViewSet):
    queryset = MachineAllocate.objects.all()
    serializer_class = MachineAllocateSerializer

    def create(self, request, *args, **kwargs):
        student = request.data.get('student')
        course = request.data.get('course')
        timeslot = request.data.get('timeslot')
        vacate = request.data.get('vacate', False)

        # Check if the student already has an allocation for the timeslot
        existing_allocation = MachineAllocate.objects.filter(student=student, timeslot=timeslot, vacate=False).first()
        if existing_allocation:
            return Response({"error": "Student already has an allocation for this timeslot."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Find an available machine for the given timeslot
        allocated_machines = MachineAllocate.objects.filter(timeslot=timeslot, vacate=False).values_list('machine', flat=True)
        available_machine = MachineAllocate.objects.exclude(id__in=allocated_machines).first()

        if not available_machine:
            return Response({"error": "No available machines for this timeslot."}, status=status.HTTP_400_BAD_REQUEST)

        # Create new allocation
        new_allocation = MachineAllocate.objects.create(
            student_id=student,
            course_id=course,
            timeslot_id=timeslot,
            machine=available_machine,
            vacate=vacate
        )

        serializer = self.get_serializer(new_allocation)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.vacate = request.data.get('vacate', instance.vacate)
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

