
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from .serializers import CheckEmailSerializer


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
    serializer_class = CheckEmailSerializer
    permission_classes = (AllowAny,)
    queryset = []

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            # Burada email ilə əməliyyat edə bilərsiniz (məsələn, bazaya qeyd)
            return Response({"email": email}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


