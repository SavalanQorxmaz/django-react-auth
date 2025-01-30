
from django.urls import path

from .views import CheckEmailGenericView, VerifyOTPGenericView
app_name = 'accounts'



urlpatterns = [
    path('api/check-email/', CheckEmailGenericView.as_view(), name='check-email'),
    path('api/verify-otp/', VerifyOTPGenericView.as_view(), name='verify-otp'),
]
