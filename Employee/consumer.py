from channels.generic.websocket import WebsocketConsumer

class employee(WebsocketConsumer):
    def connect(self):
        self.accept()
        
    def receive(self, text_data=None, bytes_data=None):
        # Called with either text_data or bytes_data for each frame
        # You can call:
        print(text_data)
        self.send(text_data="employee")
        # Or, to send a binary frame:
        self.send(bytes_data="employee")
        

    def disconnect(self, close_code):
        # Called when the socket closes
        self.close()