import environ
import pytest
from rest_framework.test import APIClient

from config import settings

env = environ.Env()

API_KEY = settings.API_KEY


@pytest.fixture
def client():
    client = APIClient()
    client.credentials(HTTP_X_API_KEY=API_KEY)
    return client
