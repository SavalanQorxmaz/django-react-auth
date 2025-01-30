
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from .serializers import CheckEmailSerializer
from utils.otp_service import OTPService


# class CheckEmailView(APIView):
#     permission_classes = (AllowAny,)
#     def post(self, request):
#         serializer = CheckEmailSerializer(data=request.data)
#         if serializer.is_valid():
#             email = serializer.validated_data['email']
#             # Burada email ilə işləyə bilərsiniz (məsələn, bazaya qeyd etmək)
#             return Response({"email": email}, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class CheckEmailGenericView(GenericAPIView):
#     serializer_class = CheckEmailSerializer
#     permission_classes = [permissions.AllowAny]
#     queryset = []

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             email = serializer.validated_data['email']
#             # Burada email ilə əməliyyat edə bilərsiniz (məsələn, bazaya qeyd)
#             return Response({"email": email}, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)class CheckEmailGenericView(GenericAPIView):
    serializer_class = CheckEmailSerializer
    permission_classes = (AllowAny,)
    queryset = []

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            
            # OTP yaradılır
            otp = OTPService.generate_otp()
            
            # OTP ilə JWT token yaradılır
            token = OTPService.create_token_with_otp(email, otp)
            
            # OTP göndərilməsi (Test məqsədli olaraq cavabda göstərilir)
            return Response({"email": email, "otp": otp, "token": token}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    
class VerifyOTPView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        token = request.data.get("token")
        otp = request.data.get("otp")

        try:
            # Tokeni doğrulayıb məlumatlarını alırıq
            access_token = AccessToken(token)
            token_otp = access_token['otp']

            if token_otp == otp:
                return Response({"detail": "OTP doğrulandı"}, status=status.HTTP_200_OK)
            else:
                return Response({"detail": "OTP yalnışdır"}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"detail": "Token etibarsızdır"}, status=status.HTTP_400_BAD_REQUEST)
