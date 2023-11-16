import re

import django.core.exceptions
from django.utils.deconstruct import deconstructible


@deconstructible
class NameValidator:
    def __init__(self, *arg):
        self.words = arg

    def __call__(self, value):
        regex = r"^[А-Я][а-я]+$"
        if re.search(regex, rf"{value}"):
            return True
        raise django.core.exceptions.ValidationError(
            "Кличка должна быть с большой буквы и "
            "иметь только русские буквы"
        )
