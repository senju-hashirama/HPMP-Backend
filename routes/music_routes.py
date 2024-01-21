from fastapi import APIRouter
from config.database import songs
from models.mongo_model import Song
from models.request_model import ReqSong
from schemas.schemas import songs_serializer,recently_played
from helper import JioSaavan

HPMP_api_router=APIRouter()

@HPMP_api_router.get("/song/{songID}")
async def get_song(songID: int):
    data=list(songs.find_one({"_id":songID}))
    if data:
        print("found")
    else:
        data=[]
    return {"status":"ok","data":data}

@HPMP_api_router.get("/search/{type}/{query}")
async def search_media(type: str,query: str):
    data=JioSaavan.search(query=query)
    if data!="Error":
        return {"status":"ok","data":data}
    else:
        return {"status":"Error"}

    
