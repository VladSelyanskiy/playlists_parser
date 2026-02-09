import json
import logging
from typing import Optional
from urllib.parse import urlparse

import requests
from requests.exceptions import RequestException, Timeout

from src.config import conf_api
from src.services.tracks_collection import TracksCollection

logger = logging.getLogger(__name__)


def get_data(
    url: Optional[str] = None,
    headers: Optional[dict] = None,
    path: Optional[str] = None,
    timeout: int = 10,
) -> Optional[TracksCollection]:

    if url is not None:
        url_path = urlparse(url).path

        if not url_path.startswith("/playlist"):
            logger.warning(f"Invalid URL path: {url_path}")
            return None

        api_url = conf_api.URL_API_KEY + url_path

        if "playlists" in api_url:
            api_url = api_url.replace("playlists", "playlist")

        try:
            response = requests.get(api_url, headers=headers, timeout=timeout)
            response.raise_for_status()
            return TracksCollection(unformatted_json=response.json())
        except Timeout:
            logger.error(f"Request timed out: {api_url}")
            return None
        except RequestException as e:
            logger.error(f"Request failed: {e}")
            return None
        except (KeyError, ValueError) as e:
            logger.error(f"Failed to parse response: {e}")
            return None

    if path is not None:
        try:
            with open(path, "r", encoding="utf-8") as file:
                return TracksCollection(unformatted_json=json.load(file))
        except (FileNotFoundError, json.JSONDecodeError) as e:
            logger.error(f"Failed to load file: {path}: {e}")
            return None

    return None
