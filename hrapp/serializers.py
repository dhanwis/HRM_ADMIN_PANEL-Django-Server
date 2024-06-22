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

class StudentStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAssign  
        fields = ['status']

class AssignProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=AssignProject
        fields='__all__'

class AssignProjectUpdateSerializer(serializers.ModelSerializer) :
    class Meta :
        model = AssignProject
        fields = ['status']

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
    


    
class NotesSharingSerializer(serializers.ModelSerializer):
    class Meta:
        model=AssignProject
        fields='__all__'

class StatusShareSerializer(serializers.ModelSerializer):
    class Meta:
        model=AssignProject
        fields='__all__'

class DigitalTableSerializer(serializers.ModelSerializer):
    class Meta:
        model=DigitalTable
        fields='__all__'

class JobApplySerializer(serializers.ModelSerializer):
    class Meta:
        model=JobApply
        fields='__all__'


class CallsheetSerializer(serializers.ModelSerializer):
    class Meta:
        model=callsheet
        fields='__all__'



class QuatationSerializer(serializers.ModelSerializer):
    class Meta:
        model=quotation
        fields='__all__'