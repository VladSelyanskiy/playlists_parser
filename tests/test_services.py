from unittest.mock import MagicMock, patch

from src.services.processing import get_data
from src.services.tracks_collection import TracksCollection


def test_tracks_collection_from_file(path_to_test_json: str, test_json_data_len: int):
    tracks_collection = get_data(path=path_to_test_json).tracks
    # check all data is loaded
    assert len(tracks_collection) == test_json_data_len
    # check types of data
    assert isinstance(tracks_collection, dict)
    assert all([isinstance(item[0], str) for item in tracks_collection.items()])
    assert all([isinstance(item[-1], list) for item in tracks_collection.items()])


@patch("requests.get")
def test_processing_good_response(mock_get):

    # make good response
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
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
    mock_get.return_value = mock_response
    # check data is loaded
    url = "https://music.yandex.ru/playlists/42?utm_source=web"
    data = get_data(url)
    assert isinstance(data, TracksCollection)
    assert data.tracks == {"test_title": ["test_artist_1"]}


@patch("requests.get")
def test_processing_bad_response(mock_get):

    # make bad response
    mock_response = MagicMock()
    mock_response.status_code = 404
    mock_response.json.return_value = {"result": "not found"}
    mock_get.return_value = mock_response
    # check data is None
    url = "https://music.yandex.ru/playlists/42?utm_source=web"
    assert get_data(url) is None


def test_proceesing_bad_url():
    assert get_data("https://example.com") is None
