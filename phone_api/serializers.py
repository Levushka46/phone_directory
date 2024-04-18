from rest_framework import serializers
from phonedb.models import PhoneNumber


class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = "__all__"


class InputPhoneNumberSerializer(serializers.Serializer):
    msisdn = serializers.CharField(max_length=11)
