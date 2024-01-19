from Admin.models import *
from Admin.constants import *
from Admin.models import COMPANY
from Employee.models import *
from datetime import datetime

def gather_data(data_no,**kwargs):
    temp = dict()
    if data_no==COMPANIES_DATA_:
        all_employ,all_present,all_absent = all_companies_data()
        temp[TO_CHECK_]=COMPANIES_DATA_
        temp[COMPANIES_DATA_]= {BALANCE_:None,EMPLOY_:all_employ,PRESENT_:all_present,ABSENT_:all_absent}
        # temp[COMPANIES_]={1:{"company_name1":"logo1"},2:{"company_name2":"logo2"}}
        temp[COMPANIES_]=all_companies_name_and_logo()
        return str(temp)
    elif data_no == COMPANY_DATA_:
        temp[TO_CHECK_]=COMPANY_DATA_
        temp[COMPANY_DATA_]= {BALANCE_:None,EMPLOY_:None,PRESENT_:None,ABSENT_:None}
        return str(temp)
    elif data_no ==EMPLOYEES_DATA_:
        temp[TO_CHECK_]=EMPLOYEES_DATA_
        temp[EMPLOYEES_DATA_]= {
                                "id1":{NAME_:None,EMAIL_:None,ROLE_:None,DEDUCTION_:None,SALARY_:None,USER_IMAGE_:None,ACCESS_:None},
                                "id2":{NAME_:None,EMAIL_:None,ROLE_:None,DEDUCTION_:None,SALARY_:None,USER_IMAGE_:None,ACCESS_:None}
                                }
        return str(temp)
    elif data_no ==ATTENDANCE_DATA_:
        # {"0":107,"107":{"15":"Emp1","16":"JAN","17":2024}}
        temp[TO_CHECK_]=ATTENDANCE_DATA_
        temp[ATTENDANCE_PROPERTIES_]= {HOURS_:None,ABSENT_:None,PRESENT_:None,PAYABLE_AMOUNT_:None,DEDUCTED_AMOUNT_:None}
        temp[MONTH_DATA_]=[{DATE_:None,CHECK_IN_:None,CHECK_OUT_:None,HOURS_:None},{DATE_:None,CHECK_IN_:None,CHECK_OUT_:None,HOURS_:None}]      
        return str(temp)
    
    print(data_no,kwargs)
    
def all_companies_data():
    all_employ = 0
    all_present = 0
    all_absent = 0
    date_time = datetime.now()
    all_employ = EMPLOYEE.objects.count()
    all_present = ATTENDANCE_REGISTER.objects.filter(date=date_time.date()).count()
    all_absent = all_employ - all_present
    return all_employ,all_present,all_absent

def all_companies_name_and_logo():
    companies =COMPANY.objects.all()
    temp_dict = {}
    for data in companies:
        temp_dict[data.id] = {data.name:data.logo}
    return temp_dict

