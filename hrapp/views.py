from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import status
from .serializers import *

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
    