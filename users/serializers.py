from rest_framework import serializers

from .models import GameUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameUser
        fields = ['id', 'username', 'hp', 'money', 'level', 'score', 'last_completed_level',
                  'archer_level', 'catapult_level', 'magic_level', 'guardian_level',
                  'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = GameUser
        fields = ['username', 'password', 'hp', 'money', 'level', 'score', 'last_completed_level',
                 'archer_level', 'catapult_level', 'magic_level', 'guardian_level']

    def create(self, validated_data):
        user = GameUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            hp=validated_data.get('hp', 100),
            money=validated_data.get('money', 1000),
            level=validated_data.get('level', 1),
            score=validated_data.get('score', 0),
            last_completed_level=validated_data.get('last_completed_level', 0),
            archer_level=validated_data.get('archer_level', 1),
            catapult_level=validated_data.get('catapult_level', 1),
            magic_level=validated_data.get('magic_level', 1),
            guardian_level=validated_data.get('guardian_level', 1)
        )
        return user

class UserUpdateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    new_username = serializers.CharField(required=False)
    
    class Meta:
        model = GameUser
        fields = ['username', 'password', 'new_username', 'hp', 'money', 'level', 'score', 'last_completed_level',
                 'archer_level', 'catapult_level', 'magic_level', 'guardian_level']
        read_only_fields = ['username']