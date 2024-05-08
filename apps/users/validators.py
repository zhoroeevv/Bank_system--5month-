import re
from django.core.exceptions import ValidationError
from rest_framework import serializers

def validate_phone_number(value):
    pattern = r'^\+996\d{9}$'
    if not re.match(pattern, value):
        raise ValidationError(
            'Номер телефона должен быть в действующим международном формате'
        )