import random
import string
from datetime import timedelta
from rest_framework_simplejwt.tokens import RefreshToken

class OTPService:
    @staticmethod
    def generate_otp():
        """6 rəqəmli təsadüfi OTP kodu yaradılır"""
        return ''.join(random.choices(string.digits, k=6))

    @staticmethod
    def create_token_with_otp(email, otp):
        """OTP və email daxilində JWT token yaradılır"""
        refresh = RefreshToken.for_user(email)  # Əgər email model istifadə etmirsinizsə, sadə bir format da ola bilər
        refresh['otp'] = otp  # OTP əlavə edilir
        refresh.set_exp(lifetime=timedelta(minutes=5))  # 5 dəqiqəlik müddət
        return str(refresh.access_token)
