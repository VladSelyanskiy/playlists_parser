from unittest.mock import MagicMock, patch

import pytest

from src.services.processing import get_data
from src.services.tracks_collection import TracksCollection


def test_tracks_collection_from_file(path_to_test_json: str, test_json_data_len: int):
    collection = get_data(path=path_to_test_json)
    tracks_collection = collection.tracks if collection is not None else {}
    # check all data is loaded
    assert len(tracks_collection) == test_json_data_len
    # check types of data
    assert isinstance(tracks_collection, dict)
    assert all([isinstance(item[0], str) for item in tracks_collection.items()])
    assert all([isinstance(item[-1], list) for item in tracks_collection.items()])


@patch("requests.get")
def test_processing_good_response(mock_get, test_data_without_metadata):

    # make good response
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = test_data_without_metadata
    mock_get.return_value = mock_response
    # check data is loaded
    url = "https://music.yandex.ru/playlists/42?utm_source=web"
    data = get_data(url)
    assert isinstance(data, TracksCollection)
    assert data.tracks == {"test_title": ["test_artist_1"]}


def test_proceesing_bad_url():
    assert get_data("https://example.com") is None


def test_tracks_collection_with_duplicates(test_data_with_duplicates):
    collection = TracksCollection(test_data_with_duplicates)
    assert "Song" in collection.tracks
    assert "Song (1)" in collection.tracks


def test_tracks_collection_invalid_structure():
    with pytest.raises(ValueError):
        TracksCollection({"invalid": "data"})


def test_tracks_collection_playlist_data(
    test_data_without_metadata, test_data_with_metadata
):
    playlist = TracksCollection(test_data_without_metadata).playlist_data
    assert all(list(map(lambda x: x is None, playlist.values())))

    playlist = TracksCollection(test_data_with_metadata).playlist_data
    assert playlist["title"] == "Title"
    assert playlist["durationMs"] == "676767"
    assert playlist["description"] is None


def test_tracks_collection_empty():
    data = {"result": {"tracks": []}}
    collection = TracksCollection(data)
    assert collection.tracks == {}
