from rest_framework import serializers
from accounts.models import User



class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_name', 'user_surname', 'user_phone', 'user_email', 'user_pass')

class ProfilePictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['profile_pic','user_surname']
        read_only_fields = ('user_surname',)

class ProfilePictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['profile_pic','user_surname']
        read_only_fields = ('user_surname',)

class ProfilePictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['profile_pic','user_surname']
        read_only_fields = ('user_surname',)

