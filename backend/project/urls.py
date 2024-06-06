from django.shortcuts import render
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/token", TokenObtainPairView.as_view(), name="obtain_token"),
    path("api/v1/token/refresh", TokenRefreshView.as_view(), name="refresh_token"),
    path("api/v1/verify/", TokenVerifyView.as_view(), name="verify_token"),
]
