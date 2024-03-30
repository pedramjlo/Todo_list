from rest_framework import serializers

from django.contrib.auth.models import User



# use models serializer if you're using other classes fields
# use serializer if you're creating fields


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


    def create(self, validate_data):
        user = User(
            email = validate_data['email'],
            username = validate_data['username']
        )
        user.set_password(validate_data['password'])
        user.save()
        return user




class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})