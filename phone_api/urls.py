from django.urls import path
from .views import phone_number_info, PhoneNumberApiView

urlpatterns = [
    path("", phone_number_info, name="phone-number-info"),
    path("phone_api/", PhoneNumberApiView.as_view(), name="phone-api-post"),
]
