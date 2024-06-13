from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import status
from .serializers import *
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ObjectDoesNotExist

######################## team lead Create #############################################################################
class TeamLeadAssignCreate(APIView):
    def get(self, request, format=None):
        team_lead = TeamleadAssign.objects.all()
        serializer = TeamLeadAssignSerializer(team_lead, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
            
    def post(self, request, format=None):
        serializer = TeamLeadAssignSerializer(data=request.data)
        if serializer.is_valid():   
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
########################### teamlead edit #################################################################################### 
class TeamLeadAssignEdit(APIView): 
     
    def get(self, request, Teamlead_id, format=None):
        team_lead = self.get_object(id=Teamlead_id)
        serializer = TeamLeadAssignSerializer(team_lead)
        return Response(serializer.data)

    def patch(self, request, Teamlead_id, format=None):
        team_lead = self.get_object(id=Teamlead_id)
        serializer = TeamLeadAssignSerializer(team_lead, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

######################## team lead Upadate ####################################################################################

class TeamLeadAssignUpdate(APIView):
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
    
############################## team lead delete ###########################################################################################   
class TeamLeadAssignDelete(APIView):
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
            return Response({"message":"Teamlead deleted successfully"},status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist:
            return Response({"error":"Teamlead not found"},status=status.HTTP_404_NOT_FOUND)

######################## student create #############################################################################      
class StudentAssignlistCreate(APIView):
    def get(self, request, format=None):
        student_assign=StudentAssign.objects.all()
        serializer= StudentAssignSerializer(student_assign,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = StudentAssignSerializer(data=request.data)
        if serializer.is_valid():   
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
########################## student task delete #########################################################################

class StudentAssignDelete(APIView):
    def get(self,request,student_id,format=None):
        try:
            student=StudentAssign.objects.get(id=student_id)
            serializer=StudentAssignSerializer(student)
            return Response(serializer.data,status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"error":"student id not found"},status=status.HTTP_404_NOT_FOUND)
    def delete(self,request,student_id,format=None):
        try:
            student=StudentAssign.objects.get(id=student_id)
            student.delete()
            return Response({"message":"Student deleted successfully"},status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist:
            return Response({"error":"Student not found"},status=status.HTTP_404_NOT_FOUND)

########################### student task update #########################################################################
   
   
class StudentAssignUpdate(APIView):
    def get(self,request,student_id,format=None):
        student=StudentAssign.objects.get(id=student_id)
        serializer=StudentAssignSerializer(student)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def patch(self,request,student_id,format=None):
        student=StudentAssign.objects.get(id=student_id)
        serializer=StudentAssignSerializer(student,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
############# project assign #########################################################################################    
   
class ProjectAssignlistCreate(APIView):
    def get(self, request, format=None):
        project_assign=ProjectAssign.objects.all()
        serializer= ProjectAssignSerializer(project_assign,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = ProjectAssignSerializer(data=request.data)
        if serializer.is_valid():   
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

########### project assign delete ###########################################################################################

class ProjectAssignDelete(APIView):
    def get(self,request,project_id,format=None):
        try:
            project=ProjectAssign.objects.get(id=project_id)
            serializer=ProjectAssignSerializer(project)
            return Response(serializer.data,status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"error":"project  not found"},status=status.HTTP_404_NOT_FOUND)
    def delete(self,request,project_id,format=None):
        try:
            project=ProjectAssign.objects.get(id=project_id)
            project.delete()
            return Response({"message":"project deleted successfully"},status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist:
            return Response({"error":" project not found"},status=status.HTTP_404_NOT_FOUND)
        
############## project upadate ################################################################################################

class projectAssignUpdate(APIView):
    def get(self,request,project_id,format=None):
        project=ProjectAssign.objects.get(id=project_id)
        serializer=ProjectAssignSerializer(project)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def patch(self,request,project_id,format=None):
        project=ProjectAssign.objects.get(id=project_id)
        serializer=ProjectAssignSerializer(project,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 










########################## digital marketing table create ###################################################################################

class DigitalTableCreate(APIView):
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
            return Response({"message":"table deleted successfully"},status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist:
            return Response({"error":" table not found"},status=status.HTTP_404_NOT_FOUND)
        









######################### team table create #########################################################################################

class TeamTableCreate(APIView):
    def get(self, request, format=None):
        team_table=TeamTable.objects.all()
        serializer= TeamTableSerializer(team_table,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = TeamTableSerializer(data=request.data)
        if serializer.is_valid():   
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    
######################### team table delete #########################################################################################

class TeamTableDelete(APIView):
    def get(self, request, team_id, format=None):
        try:
            teamtable = TeamTable.objects.get(id=team_id)
            serializer = TeamTableSerializer(teamtable)  # Use the instance instead of the class
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"error": "Team not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, team_id, format=None):
        try:
            teamtable = TeamTable.objects.get(id=team_id)
            teamtable.delete()
            return Response({"message": "Team deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist:
            return Response({"error": "Team not found"}, status=status.HTTP_404_NOT_FOUND)
        
        
        
        
        
        
        
        
        
        
        
        
##################################### leave form create #######################################################################################

class LeaveCreate(APIView):
    def get(self, request, format=None):
        leave=Leave.objects.all()
        serializer= LeaveSerializer(leave,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = LeaveSerializer(data=request.data)
        if serializer.is_valid():   
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    