from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Organization

User = get_user_model()

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']

class UserSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer(read_only=True)
    organization_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = User
        fields = [
            'id', 'first_name', 'last_name', 'email', 'phone', 'role',
            'permissions', 'organization', 'organization_id',
            'created_at', 'updated_at'
        ]

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    organization = OrganizationSerializer()

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'email', 'phone', 'role',
            'permissions', 'password', 'organization'
        ]

    def create(self, validated_data):
        org_data = validated_data.pop('organization')
        org = Organization.objects.create(**org_data)
        password = validated_data.pop('password')
        user = User.objects.create(organization=org, **validated_data)
        user.set_password(password)
        user.save()
        return user
