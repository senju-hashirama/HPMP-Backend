from pydantic import BaseModel

class ReqSong(BaseModel):
    song_id: int

class CreatePlaylist(BaseModel):
    title: str
    id: str
    userid: str
    view: str

class Info(BaseModel):
    playlist_id: str
    user_id: str
    song_id: list

class FollowPlaylist(BaseModel):
    playlist_id:str
    user_id: str
