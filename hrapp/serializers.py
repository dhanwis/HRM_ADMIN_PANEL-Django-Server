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


class AssignProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=AssignProject
        fields='__all__'

class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leave
        fields = ['start_date', 'end_date', 'description', 'duration_days', 'status']
        read_only_fields = ['duration_days', 'status']

    def create(self, validated_data):
        validated_data['name'] = self.context['request'].user
        return super().create(validated_data)

class LeaveUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leave
        fields = ['status']

class LeaveListSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source='name.username')  # Display the username
    role = serializers.ReadOnlyField(source='name.role')

    class Meta:
        model = Leave
        fields = ['id','name', 'start_date', 'end_date', 'description', 'duration_days', 'status','role']


    def get_name(self, obj):
        return obj.name.groups.first().name if obj.name.groups.exists() else 'No Role'