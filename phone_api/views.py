from django.shortcuts import render
from phonedb.models import PhoneNumber
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import InputPhoneNumberSerializer
from rest_framework import status


def get_phone_info(msisdn):
    msisdn = msisdn.lstrip("7")
    if len(msisdn) > 3:
        code = msisdn[:3]
        remaining_digits = msisdn[3:]
        try:
            phone_number = PhoneNumber.objects.get(
                code=code, start_range__lte=remaining_digits, end_range__gte=remaining_digits
            )
            return {
                "phone": msisdn,
                "operator": phone_number.operator,
                "region": phone_number.region,
                "gar_territory": phone_number.gar_territory,
                "inn": phone_number.inn,
            }
        except PhoneNumber.DoesNotExist:
            return {"error_message": "Phone number not found."}
    else:
        return {"error_message": "Invalid phone number format."}


def phone_number_info(request):
    if request.method == "POST":
        msisdn = request.POST.get("msisdn", "")
        context = get_phone_info(msisdn)
        return render(request, "phone_info.html", context)
    return render(request, "phone_form.html")


class PhoneNumberApiView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = InputPhoneNumberSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data["msisdn"]
            context = get_phone_info(phone_number)
            if "error_message" in context:
                return Response(context, status=status.HTTP_400_BAD_REQUEST)
            return Response(context, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
