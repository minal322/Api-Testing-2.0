import pytest
from utils.auth import generate_token
from utils.bookings_apis import BookingApis

@pytest.fixture(scope="session")
def apis():
    return BookingApis()

@pytest.fixture(scope="session")
def auth_token():
    return generate_token()
