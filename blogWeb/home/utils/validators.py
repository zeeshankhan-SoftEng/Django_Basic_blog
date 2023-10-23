

from django.core.exceptions import ValidationError

def validate_content_length(value):
    if len(value) > 600:
        raise ValidationError("content must be at most 600 characters long.")