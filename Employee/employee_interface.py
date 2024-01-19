from Employee.models import *
from Admin.models import COMPANY
from django.core.exceptions import ObjectDoesNotExist

def check_employee(email,company):
    try:
        employ = EMPLOYEE.objects.get(email=email,com_id = company.id)
    except ObjectDoesNotExist as er:
        print(er)
        return False
    return True


def add_employee(role,name,email,gender,password,salary,deduction,access,company_name):
    company = COMPANY.objects.get(name = company_name)
    if not check_employee(email,company):
        EMPLOYEE(name =name,email=email,gender=gender,password = password,salary = salary,deduction = deduction,access = access,com_id = company,role= role).save()
        return True
    return False

