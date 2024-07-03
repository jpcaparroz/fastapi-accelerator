import sys
import os
import uuid

import pytest

from faker import Faker

from fastapi.testclient import TestClient

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from main import app
from utils import get_config


API_VERSION = 'api/v1'
BASE_URL = f'http://{get_config('server', 'host')}:{get_config('server', 'port')}/{API_VERSION}/'

fake = Faker()


# No Rollback tests scope
@pytest.fixture(scope="function")
def test_client():
    with TestClient(app, base_url=BASE_URL) as test_client:
        yield test_client


@pytest.fixture()
def get_id() -> uuid.UUID:
    """Generate a random uuid."""
    return str(uuid.uuid4())


@pytest.fixture()
def user_payload():
    """Generate a client payload."""
    return {
        "user_name": fake.user_name(),
        "user_email": fake.email(),
        "is_admin": fake.boolean(),
        "user_password": fake.password()
    }


@pytest.fixture()
def users_payload():
    """Generate a client payload."""
    return [
        {
            "user_name": fake.name_male(),
            "user_email": fake.email(),
            "is_admin": fake.boolean(),
            "user_password": fake.password()
        },
        {
            "user_name": fake.name_female(),
            "user_email": fake.company_email(),
            "is_admin": fake.boolean(),
            "user_password": fake.password()
        }
    ]

