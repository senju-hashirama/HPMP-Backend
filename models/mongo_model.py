from pydantic import BaseModel


class Song(BaseModel):
    name: str
    song_id: int
    song_url: str
    image_url: str
    artist_names: list
    duration: int
