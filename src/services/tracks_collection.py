from typing import Optional, Any
from src.utils.processing import get_data


class TracksCollection:
    def __init__(
        self, url: Optional[str] = None, path_to_json: Optional[str] = None
    ) -> None:

        if (path_to_json is None) and (url is None):
            raise ValueError("You must provide url or path_to_json")

        if path_to_json is None:
            self._tracks: dict[Any, Any] = get_data(url)["result"]["tracks"]
        else:
            self._tracks: dict[Any, Any] = get_data(from_file=True, path=path_to_json)[
                "result"
            ]["tracks"]

        # # Create data with dict comprehension
        # self.data: dict[str, list[str]] = {
        #     track["track"]["title"]: [  # titles are keys
        #         artist["name"]
        #         for artist in track["track"]["artists"]  # lists of artists are values
        #     ]
        #     for track in self._tracks  # take data from tracks
        # }

        # Possible variant if creation data with cycle
        self.data = {}
        for track in self._tracks:

            title = track["track"]["title"]  # get title of track
            artists = [
                artist["name"] for artist in track["track"]["artists"]
            ]  # get artists of track

            if title in self.data:  # if track with same title already in data
                title += " *"  # add * to title
                self.data[title] = artists  # add track to data
            else:
                self.data[title] = artists  # add track to data


if __name__ == "__main__":
    import pprint

    pprint.pprint(len(TracksCollection(path_to_json="tests/test_data.json").data))
