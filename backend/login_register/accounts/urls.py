
from django.urls import path

from .views import CheckEmailGenericView
app_name = 'accounts'



urlpatterns = [
    path('check-email/', CheckEmailGenericView.as_view(), name='check_email'),
]
