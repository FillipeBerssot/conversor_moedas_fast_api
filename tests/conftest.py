import pytest
from fastapi.testclient import TestClient

from conversor_moedas_fast_api.app import app
from tests.fixture.converter_fixture import vcr_cassette  # noqa: F401


@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client
