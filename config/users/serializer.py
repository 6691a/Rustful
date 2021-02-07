from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    user_name = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ['email', 'user_name', 'password']
        extra_kwargs = {"password" : {"write_only" : True}}

    def create(self, validated_data):
        # user = User.objects.create_user(
        #     validated_data["email"], validated_data["user_name"], validated_data["password"]
        # )
        # return user
        password = validated_data.pop('password')
        user = self.Meta.model(**validated_data)

        if password is not None:
            user.set_password(password)

        user.save()
        return user


