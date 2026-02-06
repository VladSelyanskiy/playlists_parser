from typing import Any


class TracksCollection:
    def __init__(self, unformatted_json: dict[Any, Any]) -> None:

        self.tracks = {}  # create empty dictionary for tracks

        for track in unformatted_json["result"]["tracks"]:  # iterate through tracks

            title = track["track"]["title"]  # get title of track
            artists = [
                artist["name"] for artist in track["track"]["artists"]
            ]  # get artists of track

            if title in self.tracks:  # if track with same title already in tracks
                title += " *"  # add * to title
                self.tracks[title] = artists  # add track to tracks
            else:
                self.tracks[title] = artists  # add track to tracks

        self.playlist_data = {}  # create empty dictionary for playlist data
        for element in [
            "title",
            "description",
            "trackCount",
            "visibility",
            "created",
            "durationMs",
        ]:
            try:
                self.playlist_data[element] = str(unformatted_json["result"][element])
            except KeyError:
                self.playlist_data[element] = "not found"
                continue
