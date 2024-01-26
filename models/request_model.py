from pydantic import BaseModel
from .mongo_model import Song
class ReqSong(BaseModel):
    song_id: int

class CreatePlaylist(BaseModel):
    title: str
    userid: str
    image_url: str|None

class Info(BaseModel):
    playlist_id: str
    user_id: str
    song_info: Song

class FollowPlaylist(BaseModel):
    playlist_id:str
    user_id: str

class DeletePlaylist(BaseModel):
    playlist_id:str
    user_id: str
