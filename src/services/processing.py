import json
from typing import Optional
from urllib.parse import urlparse

import requests

from src.config import conf_api
from src.services.tracks_collection import TracksCollection


def get_data(
    url: Optional[str] = None,
    headers: Optional[dict] = None,
    path: Optional[str] = None,
) -> Optional[TracksCollection]:

    if url is not None:

        url_path = urlparse(url).path

        if not url_path.startswith("/playlist"):
            return None

        api_url = conf_api.URL_API_KEY + url_path

        if "playlists" in api_url:
            api_url = api_url.replace("playlists", "playlist")

        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            return TracksCollection(unformatted_json=response.json())
        else:
            return None

    if path is not None:
        with open(path, "r", encoding="utf-8") as file:
            return TracksCollection(unformatted_json=json.load(file))

    return None
