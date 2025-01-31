from django.core.cache import cache
from datetime import datetime
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from users.serializers.email_otp_serializer import CheckEmailSerializer, CheckOTPSerializer
from utils.otp_service import OTPService
from utils.constants import OTP_LIFE_TIME


class CheckEmailGenericView(GenericAPIView):
    serializer_class = CheckEmailSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        print("Hello")
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            try:
                otp = cache.get(f"otp_{email}")
                otp_created_at = cache.get(f"otp_created_at_{email}")
                remaining_time = OTPService.get_remaining_time(otp_created_at)

                if not otp or remaining_time == OTP_LIFE_TIME:
                    otp = OTPService.generate_otp()
                    otp_created_at = datetime.now()

                    cache.set(f"otp_{email}", otp, timeout=remaining_time)
                    cache.set(f"otp_created_at_{email}", otp_created_at, timeout=remaining_time)
                    OTPService.send_otp_via_email(email, otp, remaining_time)

                token = OTPService.create_token_with_otp(email, otp, remaining_time)
                return Response({"email": email, "otp": otp, "token": token, "message": "OTP kodu göndərildi."}, status=status.HTTP_200_OK)


            except Exception as e:
                return Response({"error": "Daxili server xətası."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    
class VerifyOTPGenericView(GenericAPIView):
    serializer_class = CheckOTPSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            otp = serializer.validated_data['otp']

            # Cache-dən OTP-ni oxuyuruq
            cached_otp = cache.get(f"otp_{email}")

            if cached_otp and cached_otp == otp:
                # OTP doğrulandı, cache-dən silirik
                cache.delete(f"otp_{email}")
                return Response({"message": "OTP uğurla təsdiqləndi."}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Yanlış və ya vaxtı keçmiş OTP."}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)