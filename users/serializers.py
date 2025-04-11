from rest_framework import serializers

from .models import GameUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameUser
        fields = ['id', 'username', 'display_name', 'hp', 'money', 'start_hp', 'start_money', 'last_completed_level',
                  'tutorial_complete', 'archer_level', 'catapult_level', 'magic_level', 
                  'guardian_level', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    
    class Meta:
        model = GameUser
        fields = ['username', 'display_name', 'password', 'confirm_password']

    def validate(self, data):
        # Validasi password dan confirm_password cocok
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords don't match")
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')  # Hapus confirm_password dari data
        user = GameUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            display_name=validated_data['display_name']
        )
        return user

class UserUpdateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    new_username = serializers.CharField(required=False)
    
    class Meta:
        model = GameUser
        fields = ['username', 'password', 'new_username', 'display_name', 'hp', 'money', 'start_hp', 'start_money',
                 'last_completed_level', 'tutorial_complete', 'archer_level', 
                 'catapult_level', 'magic_level', 'guardian_level']
        read_only_fields = ['username']