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


@pytest.fixture()
def test_data_with_duplicates():
    return {
        "result": {
            "tracks": [
                {
                    "track": {
                        "title": "Song",
                        "artists": [{"name": "Artist1"}],
                    }
                },
                {
                    "track": {
                        "title": "Song",
                        "artists": [{"name": "Artist2"}],
                    }
                },
            ]
        }
    }


@pytest.fixture()
def test_data_without_metadata():
    return {
        "result": {
            "tracks": [
                {
                    "track": {
                        "title": "test_title",
                        "artists": [{"name": "test_artist_1"}],
                    }
                }
            ]
        }
    }


@pytest.fixture()
def test_data_with_metadata():
    return {
        "result": {
            "tracks": [
                {
                    "track": {
                        "title": "test_title",
                        "artists": [{"name": "test_artist_1"}],
                    }
                }
            ],
            "title": "Title",
            "durationMs": 676767,
        }
    }
