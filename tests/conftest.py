import os

import pytest
from fastapi.testclient import TestClient

from src.main import app


@pytest.fixture()
def client():
    return TestClient(app)


@pytest.fixture()
def path_to_test_json():
    return os.path.join(os.path.dirname(__file__), "test_data.json")


@pytest.fixture()
def test_json_data_len():
    return 449
