from django.conf import settings

if not settings.configured:
    settings.configure(
        CACHES={
            'default': {
                'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
                'LOCATION': 'unique-snowflake',
            }
        }
    )

from django.core.cache import cache
from datetime import datetime, timedelta

# cache.set("otp_test@example.com", "123456", timeout=300)
# print(cache.get("otp_test@example.com"))  # '123456' qaytarmalıdır.


now = datetime.now()
tomorrow = now + timedelta(seconds=3000)

print((tomorrow - now).total_seconds(), timedelta(seconds=3000))