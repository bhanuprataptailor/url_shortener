from ..models import CoreMapping
from django.conf import settings


def _get_mapping():
    mapping = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}

    start_i = 10
    N = 26
    for idx in range(97, 97 + N):
        mapping[start_i] = chr(idx)
        start_i += 1
    N = 26
    for idx in range(65, 65 + N):
        mapping[start_i] = chr(idx)
        start_i += 1
    return mapping


def _calculate_base62(num):
    base64 = ''
    mapping = _get_mapping()
    while num > 0:
        remainder = num % 62
        base64 = str(mapping[remainder]) + base64
        num = num // 62

    return base64


def generate_unique_key():
    try:
        value = CoreMapping.objects.all().last().counter
    except:
        value = settings.CORE_COUNTER_START
    return _calculate_base62(value)