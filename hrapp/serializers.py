from rest_framework import serializers
from .models import *



class TeamLeadAssignSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamleadAssign
        fields = '__all__'
        # extra_kwargs = {'password':{'write_only':True}}
        
        
class StudentAssignSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAssign
        fields = '__all__'
        

class ProjectAssignSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectAssign
        fields = '__all__'
        
class DigitalTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = DigitalTable
        fields = '__all__'
        
class TeamTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamTable
        fields = '__all__'
        
class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leave
        fields = '__all__'