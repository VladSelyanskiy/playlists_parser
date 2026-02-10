from pydantic import BaseModel, Field


class TracksOutput(BaseModel):
    tracks: dict[str, list[str]] = Field(
        default_factory={"track": ["artist-1", "artist-n"]},
        description="List of track and artists",
    )

    playlist_data: dict[str, str | None] = Field(
        default_factory={
            "title": None,
            "description": None,
            "trackCount": None,
            "visibility": None,
            "created": None,
            "durationMs": None,
        },
        description="Playlist metadata",
    )
