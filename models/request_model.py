from pydantic import BaseModel
from datetime import date
from .mongo_model import Song
class ReqSong(BaseModel):
    song_id: int

class CreatePlaylist(BaseModel):
    title: str
    userid: str
    image_url: str|None
    doc: str
    model_config={
        "json_schema_extra":{
            "examples":[
                    {
                        "title": "Test",
                        "userid":"k2ub9bPkE0WE1Ob64wPtnLhMBUi2",
                        "image_url":"Blah",
                        "doc": "2024-1-28"
                    }
            ]
        }
    }


class Info(BaseModel):
    playlist_id: str
    user_id: str
    song_info: Song
    model_config={
        "json_schema_extra":{
            "examples":[
                    {
                        "user_id":"k2ub9bPkE0WE1Ob64wPtnLhMBUi2",
                        "playlist_id":"",
                        "song_info":{
                                "title": "Maharani",
                                "subtitle": "Karun, Lambo Drive ft. Arpit Bala, ReVo LEKHAK - Maharani",
                                "song_url": "https://aac.saavncdn.com/925/b96d1bd3dbd2bd466a605a7850ff3cc9_96.mp4",
                                "image_url": "https://c.saavncdn.com/925/Maharani-Hindi-2021-20220211204609-150x150.jpg",
                                "artist_names": [
                                    "Karun",
                                    "Lambo Drive"
                                ],
                                "duration": "389",
                                "id": "ZpVOC8H0"
                        }
                    }
            ]
        }
    }

class FollowPlaylist(BaseModel):
    playlist_id:str
    user_id: str

class DeletePlaylist(BaseModel):
    playlist_id:str
    user_id: str
    model_config={
        "json_schema_extra":{
            "examples":[
                    {
                        "user_id":"k2ub9bPkE0WE1Ob64wPtnLhMBUi2",
                        "playlist_id":""
                    }
            ]
        }
    }


class DeletePlaylistTrack(BaseModel):
    playlist_id:str
    user_id: str
    song_id: str
    model_config={
        "json_schema_extra":{
            "examples":[
                    {
                        "user_id":"k2ub9bPkE0WE1Ob64wPtnLhMBUi2",
                        "song_id":"ZpVOC8H0",
                        "playlist_id":""
                    }
            ]
        }
    }


class SetRecentlyPlayed(BaseModel):
    user_id: str
    song: Song

    model_config={
        "json_schema_extra":{
            "examples":[
                    {
                        "user_id":"k2ub9bPkE0WE1Ob64wPtnLhMBUi2",
                        "song": {
                             "title": "Maharani",
                                "subtitle": "Karun, Lambo Drive ft. Arpit Bala, ReVo LEKHAK - Maharani",
                                "song_url": "https://aac.saavncdn.com/925/b96d1bd3dbd2bd466a605a7850ff3cc9_96.mp4",
                                "image_url": "https://c.saavncdn.com/925/Maharani-Hindi-2021-20220211204609-150x150.jpg",
                                "artist_names": [
                                    "Karun",
                                    "Lambo Drive"
                                ],
                                "duration": "389",
                                "id": "ZpVOC8H0"
                        }
                    }
            ]
        }
    }




class GetPlaylist(BaseModel):
    playlist_id: str
    user_id: str