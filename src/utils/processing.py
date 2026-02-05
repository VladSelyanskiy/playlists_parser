import json
from typing import Any, Optional
from urllib.parse import urlparse

import requests

from src.config import conf_api


def get_data(
    url: Optional[str] = None,
    from_file: bool = False,
    headers: Optional[dict] = None,
    path: Optional[str] = None,
) -> dict[Any, Any]:
    if from_file:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    else:
        api_url = conf_api.URL_API_KEY + urlparse(url).path
        if "playlists" in api_url:
            api_url = api_url.replace("playlists", "playlist")
        response = requests.get(api_url, headers=headers)
        return response.json()
