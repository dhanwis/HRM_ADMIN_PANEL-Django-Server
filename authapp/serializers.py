from rest_framework import serializers
from .models import *
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class InstallmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Installments
        fields = ['amount', 'date']

class InternSerializer(serializers.ModelSerializer):
    installments = InstallmentSerializer(many=True, required=False)

    class Meta:
        model = UserProfile
        fields = [
            'university',
            'degree_program',
            'internship_position',
            'start_date',
            'end_date',
            'category',
            'payment',
            'payment_date',
            'total_amount',
            'no_of_installments',
            'installments'
        ]

    def create(self, validated_data):
        installments_data = validated_data.pop('installments', [])
        user_profile = UserProfile.objects.create(**validated_data)
        for installment_data in installments_data:
            Installments.objects.create(user_profile=user_profile, **installment_data)
        return user_profile


class UserInternSerializer(serializers.ModelSerializer):
    profile = InternSerializer(write_only=True)

    class Meta:
        model = User
        fields = [
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
        installments_data = profile_data.pop('installments', [])  # Extract installments data if present

        # Create User instance
        user = User.objects.create_user(**validated_data)
        user.is_intern = True
        user.save()

        # Create UserProfile instance
        user_profile = UserProfile.objects.create(user=user, **profile_data)

        # Create Installments instances and associate them with UserProfile
        for installment_data in installments_data:
            Installments.objects.create(user_profile=user_profile, **installment_data)

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




