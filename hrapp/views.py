from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import status
from .serializers import *
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
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




class TeamLeadDelete(APIView):
    def get(self,request,teamlead_id,format=None):
        try:
           team_lead=TeamleadAssign.objects.get(id=teamlead_id)
           serializer=TeamLeadAssignSerializer(team_lead)
           return Response(serializer.data,status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"error":"teamlead not found"},status=status.HTTP_404_NOT_FOUND)
    def delete(self,request,teamlead_id,format=None):
        try:
            team_lead = TeamleadAssign.objects.get(id=teamlead_id)
            team_lead.delete()
            return Response({"message": "Team lead deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist:
            return Response({"error": "Team lead not found."}, status=status.HTTP_404_NOT_FOUND)

    

# class ProjectAssignCreate(APIView):
#     def get(self, request, format=None):
#         project_assign= ProjectAssign.objects.all()
#         serializer = ProjectAssignSerializer(project_assign, many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
            
#     def post(self, request, format=None):
#         serializer = ProjectAssignSerializer(data=request.data)
#         if serializer.is_valid():   
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
