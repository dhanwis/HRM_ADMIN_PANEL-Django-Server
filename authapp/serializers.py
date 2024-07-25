from rest_framework import serializers
from .models import *
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields='__all__'
        fields=['id','username','password','image','dob','email','pincode','department','state','country','city','address','phone_number','experience','role']
        extra_kwargs = {'password': {'write_only': True}}
        

    def create(self, validated_data):
        
        user = User.objects.create_user(**validated_data)
        return user

class InternSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            'educationalQualification',
            'course',
            'start_date',
            'end_date',
            'category',
            'payment',
            'payment_date',
            'total_amount',
            'no_of_installments'
        ]

class UserInternSerializer(serializers.ModelSerializer):
    profile = InternSerializer(write_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'phone_number',
            'address',
            'dob',
            'city',
            'state',
            'country',
            'pincode',
            'password',
            'profile'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create_user(**validated_data)
        user.save()
        user_profile = UserProfile.objects.create(user=user, **profile_data)
        user_profile.save()
        return user
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        profile_data = InternSerializer(instance.userprofile).data
        representation['profile'] = profile_data
        return representation
    


class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reference
        fields='__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model=Feedback
        fields='__all__'


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model=Testimonial
        fields='__all__'
        