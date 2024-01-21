from fastapi import APIRouter,HTTPException,Request
from config.database import users
from schemas.schemas import playlist, recently_played
from models.request_model import CreatePlaylist,Info,FollowPlaylist
from helper.FirebaseAuth import Verify_Token

user_router=APIRouter()





@user_router.get("/recently_played/{userID}")
async def get_recebtly_played(userID:str):
    data=users.find_one({"_id":userID})
    return recently_played(data["recently_played"])

@user_router.get("/get_playlist/{playlistID}")
async def playlist_get(playlistID:str):
    data=users.find({"_id":playlistID})
    return playlist(data)

@user_router.post("/create_playlist")
async def playlist_create(playlist_info: CreatePlaylist):
    #Create playlist after making necessary checks
    return {"status":"Not implemented"}

@user_router.post("/update_playlist_song")
async def update_playlist_(info: Info):
    #Add playlist info
    return {"status":"Not implemented"}

@user_router.post("/follow_playlist")
async def playlist_follow(follow_request:FollowPlaylist):
    #Follow a particular playlist
    return {"status":"Not implemented"}