from http.client import responses

import requests
import json

class BookingApis:

    def __init__(self):
        self.header = {
            "Content-Type" : "application/json"
        }
        self.baseUrl = "https://restful-booker.herokuapp.com"

    def merge_header(self,custom_headers = None):
        if custom_headers:
            temp_headers = self.header.copy()
            temp_headers.update(custom_headers)
            return temp_headers
        return self.header


    def get(self,endpoint,custom_headers=None):
        get_url = self.baseUrl + endpoint
        response = requests.get(url=get_url,headers=self.merge_header(custom_headers))
        return response

    def post(self,endpoint,request_body,custom_headers=None):
        post_url = self.baseUrl +endpoint
        response = requests.post(url=post_url,headers=self.merge_header(custom_headers),json = request_body)
        return response

    def put(self,endpoint,request_body,custom_headers=None):
        put_url = self.baseUrl + endpoint
        response = requests.put(url = put_url,headers=self.merge_header(custom_headers),json = request_body)
        return response

    def patch(self,endpoint,request_body, custom_headers= None):
        patch_url = self.baseUrl+endpoint
        response = requests.patch(url = patch_url,headers=self.merge_header(custom_headers),json=request_body)
        return response

    def delete(self,endpoint,custom_headers=None):
        delete_url = self.baseUrl+endpoint
        response = requests.delete(url=delete_url,headers=self.merge_header(custom_headers))
        return response