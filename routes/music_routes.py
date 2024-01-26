from fastapi import APIRouter
from config.database import songs
from models.mongo_model import Song
from models.request_model import ReqSong
from schemas.schemas import songs_serializer,recently_played
from helper import JioSaavan

HPMP_api_router=APIRouter()

@HPMP_api_router.get("/song/{songID}")
async def get_song(songID: str):
    try:
        res=songs.find_one({"_id":songID})
        if res:
            data=songs_serializer(res)
            return {"status":"ok","data":data}
        else:
            return {"status":"error","data":"Not found"}    
    except Exception as E:
        
        return {"status":"error","data":str(E)}

@HPMP_api_router.get("/search/{query}")
async def search_media(query: str):
    data=JioSaavan.search(query=query)
    if data!="Error":
        return {"status":"ok","data":data}
    else:
        return {"status":"Error"}

    
