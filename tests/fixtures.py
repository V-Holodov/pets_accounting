import environ
import pytest
from rest_framework.test import APIClient

env = environ.Env()

API_KEY = env.str("API_KEY_SECRET")


@pytest.fixture
def client():
    client = APIClient()
    client.credentials(HTTP_X_API_KEY=API_KEY)
    return client
