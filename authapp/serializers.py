from rest_framework import serializers
from .models import User, UserProfile
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class InternSerializer(serializers.ModelSerializer):
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
            'no_of_installments'
        ]

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
        user = User.objects.create_user(**validated_data)
        user.is_intern = True
        user.save()
        user_profile = UserProfile.objects.create(user=user, **profile_data)
        user_profile.save()
        return user
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        profile_data = InternSerializer(instance.userprofile).data
        representation['profile'] = profile_data
        return representation