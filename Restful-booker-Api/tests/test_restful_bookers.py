import pytest

booking_id = 1

def test_get_all_booking_ids(apis,auth_token):
    response = apis.get("/booking")
    assert response.status_code == 200
   # print(response.json())

def test_create_booking(apis,auth_token):
    global booking_id
    req_payload = {
        "firstname": "Akshata",
        "lastname": "Patil",
        "totalprice": 2000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-01-09",
            "checkout": "2025-01-20"
        },
        "additionalneeds": "Lunch"
    }
    response = apis.post("/booking",req_payload)
    assert response.status_code in  [200,201]
    booking_id = response.json()["bookingid"]

    assert req_payload["firstname"] == response.json()["booking"]["firstname"]
    assert req_payload["lastname"] == response.json()["booking"]["lastname"]
    assert req_payload["additionalneeds"] == response.json()["booking"]["additionalneeds"]
    assert req_payload["depositpaid"] == response.json()["booking"]["depositpaid"]
    assert req_payload["totalprice"] == response.json()["booking"]["totalprice"]
    assert req_payload["bookingdates"]["checkin"] == response.json()["booking"]["bookingdates"]["checkin"]
    assert req_payload["bookingdates"]["checkout"] == response.json()["booking"]["bookingdates"]["checkout"]

def test_get_specific_booking(apis):
    global booking_id
    response = apis.get(f"/booking/{booking_id}")
    assert response.status_code == 200
    print(response.json())

def test_update_booking_details(apis,auth_token):
    global booking_id
    req_payload = {
        "firstname": "Minal",
        "lastname": "Patil",
        "totalprice": 2000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-01-09",
            "checkout": "2025-01-25"
        },
        "additionalneeds": "Breakfast"
    }
    header = {
        "Accept" : "application/json",
        "cookie" : f"token={auth_token}",
        "Authorization" : "basic"
    }
    response = apis.put(f"/booking/{booking_id}",req_payload,custom_headers=header )
    assert response.status_code == 200
    print(response.json())
    assert req_payload["firstname"] == response.json()["firstname"]
    assert req_payload["lastname"] == response.json()["lastname"]
    assert req_payload["additionalneeds"] == response.json()["additionalneeds"]
    assert req_payload["depositpaid"] == response.json()["depositpaid"]
    assert req_payload["totalprice"] == response.json()["totalprice"]
    assert req_payload["bookingdates"]["checkin"] == response.json()["bookingdates"]["checkin"]
    assert req_payload["bookingdates"]["checkout"] == response.json()["bookingdates"]["checkout"]

def test_partialUpdate_booking_details(apis,auth_token):
    global booking_id
    req_payload = {
        "firstname": "Meenal",
        "lastname": "Patil",
    }
    header = {
        "Accept" : "application/json",
        "cookie" : f"token={auth_token}",
        "Authorization" : "basic"
    }
    response = apis.patch(f"/booking/{booking_id}",req_payload,custom_headers=header )
    assert response.status_code == 200
    print(response.json())
    assert req_payload["firstname"] == response.json()["firstname"]
    assert req_payload["lastname"] == response.json()["lastname"]

def test_delete_booking(apis,auth_token):
    global booking_id
    header = {
        "Accept": "application/json",
        "cookie": f"token={auth_token}"
    }
    response = apis.delete(f"/booking/{booking_id}",custom_headers=header)
    assert response.status_code == 201

def test_health_check(apis):
    response = apis.get("/ping")
    assert response.status_code == 201