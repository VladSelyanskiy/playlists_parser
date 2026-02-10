import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)


class TracksCollection:
    def __init__(self, unformatted_json: dict[Any, Any]) -> None:
        self.tracks: dict[str, list[str]] = {}  # create empty dictionary for tracks

        try:
            tracks_data = unformatted_json["result"]["tracks"]
        except KeyError:
            raise ValueError("Invalid Json structure: missing 'result.tracks'")

        for track in tracks_data:  # iterate through tracks
            try:
                title = track["track"]["title"]  # get title of track
                artists = [
                    artist["name"] for artist in track["track"]["artists"]
                ]  # get artists of track

                counter = 1
                original_title = title
                while (
                    title in self.tracks
                ):  # if track with same title already in tracks
                    title = f"{original_title} ({counter})"  # add counter to title
                    counter += 1

                self.tracks[title] = artists  # add track to tracks
            except KeyError as e:
                logger.warning(f"Skipping invalid track: {e}")
                continue

        self.playlist_data: dict[str, Optional[str]] = self._extract_playlist_metadata(
            data=unformatted_json
        )

    def _extract_playlist_metadata(
        self, data: dict[Any, Any]
    ) -> dict[str, Optional[str]]:
        metadata_fields = [
            "title",
            "description",
            "trackCount",
            "visibility",
            "created",
            "durationMs",
        ]
        playlist_data: dict[str, Optional[str]] = {}

        for field in metadata_fields:
            try:
                playlist_data[field] = str(data["result"][field])
            except KeyError:
                playlist_data[field] = None
                continue

        return playlist_data
