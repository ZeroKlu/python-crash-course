from distutils.command.clean import clean
from urllib import response
import requests
import uuid

class WebServiceCall:
    def __init__(self, url = "http://onbasetestvm/LocationLookupService/ExampleWebService.svc/Web/LookupLocationRest"):
        self.url = url

    def call_service(self, lookup_value):
        request_id = uuid.uuid4()
        ws_url = f"{self.url}/{request_id}/{lookup_value}"
        response = requests.get(ws_url)
        if response.status_code != 200:
            return f"ERROR: Status = {response.status_code}"
        return response.text.split('>')[1].split('<')[0]
