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