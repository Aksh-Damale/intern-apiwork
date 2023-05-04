from fastapi.encoders import jsonable_encoder
from datetime import datetime

class APIResponse:

    # Constructor to set response param like message, status code & payload(data)
    def __init__(self, message, status_code=None, payload=None):
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload
        self.timestamp = datetime.now()

    # Function to get the response back in json format
    def get_response(self):
        response = {}
        response['status_code'] = self.status_code
        response['message'] = self.message
        response['timestamp'] = self.timestamp
        if self.payload is not None:
            response['data'] = self.payload 
        else:
            response['data'] = "No Data Available"
        return jsonable_encoder(response)