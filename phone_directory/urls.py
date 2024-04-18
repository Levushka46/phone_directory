from django.contrib import admin
from django.urls import path, include
from phone_api import urls as phone_api_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(phone_api_urls)),
]
