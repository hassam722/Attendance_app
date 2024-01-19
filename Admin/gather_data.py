from Admin.models import *
from Admin.constants import *


def gather_data(data_no,**kwargs):
    temp = dict()
    if data_no==COMPANIES_DATA_:
        temp[TO_CHECK_]=COMPANIES_DATA_
        temp[COMPANIES_DATA_]= {BALANCE_:None,EMPLOY_:None,PRESENT_:None,ABSENT_:None}
        temp[COMPANIES_]={"company_name":"logo"}
        return str(temp)
    print(data_no,kwargs)
    pass