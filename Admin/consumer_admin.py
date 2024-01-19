from channels.generic.websocket import WebsocketConsumer
import json
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
            data = json_data.get(str(LOGIN_))
            flag = authenticate(data.get(str(EMAIL_)),data.get(str(PASSWORD_)))
            if flag:
                data = gather_data(COMPANIES_DATA_,email = "hassam",password = "password")
                self.send(text_data=gather_data)
            else:
                self.send(text_data=give_message(203))
        elif to_check==CREATE_:
            data = json_data.get(str(CREATE_))
            flag =create_admin(data.get(str(NAME_)),data.get(str(EMAIL_)),data.get(str(PASSWORD_)))
            if flag:
                self.send(text_data=give_message(201))
            else:
                self.send(text_data=give_message(202))

                      

        self.send(text_data="Hello world!")
        # Or, to send a binary frame:
        # self.send(bytes_data=b'Hello world!')
        

    def disconnect(self, close_code):
        # Called when the socket closes
        self.close()