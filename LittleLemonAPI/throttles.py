from rest_framework.throttling import AnonRateThrottle
from django.core.cache import cache

class OneCallPerMinute(AnonRateThrottle):
    scope = "one"