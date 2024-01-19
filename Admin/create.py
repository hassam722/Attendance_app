from Admin.login import authenticate
from Admin.models import ADMIN


def create_admin(admin_name,admin_email,admin_password):
    check_admin = authenticate(admin_email,admin_password)
    if not check_admin:
        admin = ADMIN(name = admin_name,email = admin_email,password = admin_password)
        admin.save()
        return True
    else:
        return False