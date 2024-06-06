from rest_framework import serializers
from .models import *



class TeamLeadAssignSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamleadAssign
        fields = '__all__'
        # extra_kwargs = {'password':{'write_only':True}}

# class ProjectAssignSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=ProjectAssign
#         fields='__all__'