from pydantic import BaseModel


class Song(BaseModel):
    id: str
    title: str
    subtitle: str
    song_url: str
    image_url: str
    artist_names: list
    duration: int

