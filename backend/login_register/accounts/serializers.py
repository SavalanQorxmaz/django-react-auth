from rest_framework import serializers


class CheckEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()

class CheckOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(min_length=6, max_length=6)