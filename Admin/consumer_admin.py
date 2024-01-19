from channels.generic.websocket import WebsocketConsumer
import json
from Employee.employee_interface import add_employee
from Admin.constants import *
from Admin.login import *
from Admin.create import *
from Admin.message import *
from Admin.gather_data import *
class admin(WebsocketConsumer):
    def connect(self):
        self.accept()
        
    def receive(self, text_data=None):
        json_data = json.loads(text_data)
        to_check = json_data.get(str(TO_CHECK_))
        print(json_data)
        if to_check==LOGIN_:
            # {"0":101,"101":{"1":"haider.khan@sclera.at","2":"password"}}
            data = json_data.get(str(LOGIN_))
            flag = authenticate(data.get(str(EMAIL_)),data.get(str(PASSWORD_)))
            if flag:
                # here also creating a session for admin
                data = gather_data(COMPANIES_DATA_)
                self.send(text_data=data)
            else:
                self.send(text_data=give_message(203))
        elif to_check==CREATE_:# this command works only once at the time of creation in one whole project.
            data = json_data.get(str(CREATE_))
            flag =create_admin(data.get(str(NAME_)),data.get(str(EMAIL_)),data.get(str(PASSWORD_)))
            if flag:
                self.send(text_data=give_message(201))
            else:
                self.send(text_data=give_message(202))
        elif to_check==COMPANY_DATA_:
            # {'0': 105, '105': {'4': 'COMPANY1'}}
            data = json_data.get(str(COMPANY_DATA_))
            company_data = gather_data(COMPANY_DATA_,company_name = data.get(str(NAME_)))
            self.send(text_data=company_data)
        elif to_check ==EMPLOYEES_DATA_:
            # {'0': 106, '106': {'4': 'COMPANY1'}}
            data = json_data.get(str(EMPLOYEES_DATA_))
            employees_data = gather_data(EMPLOYEES_DATA_,company_name = data.get(str(NAME_)))
            self.send(employees_data)
        elif to_check ==ATTENDANCE_DATA_:
            # {'0': 107, '107': {'15': 'EMP1'}}
            data = json_data.get(str(ATTENDANCE_DATA_))
            attendance_data = gather_data(ATTENDANCE_DATA_,employ_id = data.get(str(ID_)),month = data.get(str(MONTH_)),year = data.get(str(YEAR_)))
            self.send(attendance_data)
        elif to_check ==ADD_EMPLOYEE_:
            # {"0": 108, "108": {"10": "developer","4":"hassam","2":"password","1":"hassamghori722@gmail.com","26":"male","12":45000,"13":1000,"11":"ADMIN","3":"COMPANY1"}}
            data = json_data.get(str(ADD_EMPLOYEE_))
            flag = add_employee(
                                data.get(str(ROLE_)),data.get(str(NAME_)),
                                data.get(str(EMAIL_)),data.get(str(GENDER_)),
                                data.get(str(PASSWORD_)),data.get(str(SALARY_)),
                                data.get(str(DEDUCTION_)),data.get(str(ACCESS_)),
                                data.get(str(COMPANY_NAME_))
                                )
            if flag:
                self.send(text_data=give_message(204))
            else:
                self.send(text_data=give_message(202))


                      

        # self.send(text_data="Hello world!")
        # Or, to send a binary frame:
        # self.send(bytes_data=b'Hello world!')
        

    def disconnect(self, close_code):
        # Called when the socket closes
        self.close()