from django.urls import path

from .views.email_otp_views import CheckEmailGenericView, VerifyOTPGenericView


app_name = 'users'


urlpatterns = [
    path('check-email/', CheckEmailGenericView.as_view(), name='check-email'),
    path('verify-otp/', VerifyOTPGenericView.as_view(), name='verify-otp'),
]
