import json
import requests

def generate_token():
    token_url ="https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    body = {
                        "username" : "admin",
                        "password" : "password123"
                      }
    response = requests.post(url=token_url,headers=headers,data=json.dumps(body))
    return response.json()["token"]



