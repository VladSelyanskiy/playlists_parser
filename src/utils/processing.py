import requests
import json
from typing import Optional, Any


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
        response = requests.get(url, headers=headers)
        return response.json()


if __name__ == "__main__":
    import pprint

    pprint.pprint(
        len(get_data(from_file=True, path="tests/test_data.json")["result"]["tracks"])
    )
