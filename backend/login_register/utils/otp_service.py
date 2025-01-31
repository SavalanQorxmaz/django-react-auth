import random
import string
from django.core.mail import send_mail
from django.conf import settings
from datetime import timedelta, datetime
from rest_framework_simplejwt.tokens import AccessToken
from utils.constants import OTP_LIFE_TIME
from dotenv import load_dotenv

class OTPService:
    @staticmethod
    def generate_otp():
        return ''.join(random.choices(string.digits, k=6))
    
    @staticmethod
    def get_remaining_time(created_at):
        if not created_at:
            return OTP_LIFE_TIME
        now = datetime.now()
        time_passed = (now - created_at).total_seconds()
        remaining_time = OTP_LIFE_TIME - time_passed
        print('remaining_time: ',remaining_time)
        if remaining_time < 60:
            return OTP_LIFE_TIME
        return  remaining_time

    @staticmethod
    def create_token_with_otp(email, otp, seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        """User olmadan OTP üçün JWT token yaradır"""
        access = AccessToken()
        access["email"] = email
        access["otp"] = otp
        access.set_exp(lifetime=timedelta(minutes=minutes, seconds=seconds)) 
        return str(access)
    
    @staticmethod
    def send_otp_via_email(email, otp, seconds):
        """OTP kodunu istifadəçiyə göndərir"""
        print(settings.BASE_DIR)
        print(settings.DEFAULT_FROM_EMAIL)
        minutes = seconds // 60
        seconds = seconds % 60
        subject = "Sizin OTP Kodu"
        message = f"Sizin təsdiq kodunuz: {otp}.\nKod {minutes} dəqiqə : {seconds} saniyə ərzində etibarlıdır."
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [email]

        send_mail(subject, message, from_email, recipient_list, fail_silently=False)