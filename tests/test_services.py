from src.services.tracks_collection import TracksCollection


def test_tracks_collection_from_file(path_to_test_json, test_json_data_len):
    tracks_collection = TracksCollection(path_to_json=path_to_test_json).data
    assert len(tracks_collection) == test_json_data_len
    assert all([isinstance(item[0], str) for item in tracks_collection.items()])
    assert all([isinstance(item[-1], list) for item in tracks_collection.items()])
