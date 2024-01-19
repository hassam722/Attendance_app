from Admin.models import ADMIN
from django.core.exceptions import ObjectDoesNotExist


def authenticate(email,password):
    try:
        admin = ADMIN.objects.get(email=email,password=password)
    except ObjectDoesNotExist as er:
        print(er)
        return False
    return True
    