from fastapi import APIRouter,HTTPException,Request
from config.database import users,playlists,songs
from schemas.schemas import playlist, recently_played, user_playlists
from models.request_model import CreatePlaylist,Info,FollowPlaylist, DeletePlaylist
from helper.FirebaseAuth import Verify_Token
from pymongo import errors
from bson import ObjectId
user_router=APIRouter()





@user_router.get("/recently_played/{user_id}")
async def get_recebtly_played(user_id:str,request:Request):
    
    data=users.find_one({"_id":user_id})
    return recently_played(data["recently_played"])

@user_router.get("/get_playlists/{user_id}")
async def get_user_playlists(user_id:str):
    
        p=playlists.find({"user_id":user_id})
        
        data=user_playlists(p)
        print("playlists",data)
        
        return {"status":"ok","data":data}
    
@user_router.get("/get_playlist/{playlistID}")
async def playlist_get(playlistID:str,request:Request):
    # try:
    #     # data=users.find({"_id":request.headers.get("user")[""]})
    #     return {"status":"ok","data":[playlistID]}
    # except Exception as E:
    #     print(E)
    #     return {"status":"error","data":E}
    return {"Status":"Not implemented"}

@user_router.post("/create_playlist")
async def playlist_create(playlist_info: CreatePlaylist,request: Request):
    
    userID=playlist_info.userid
    playlist_id=playlists.insert_one({"title":playlist_info.title,"user_id":playlist_info.userid,"songs":[],"image_url":playlist_info.image_url})
    res=users.update_one({"_id":userID},{"$push":{"playlists":playlist_id.inserted_id}})

    if res.modified_count>0:
        return {"status":"ok"}
    else:
        return {"status":"error"}

@user_router.post("/add_playlist_song")
async def update_playlist(info: Info):
    track=info.song_info
    
    try:
        song_id=songs.insert_one({"_id":track.id,"title":track.title,"song_url":track.song_url,"image_url":track.image_url,"artist_names":track.artist_names,"duration":track.duration,"subtitle":track.subtitle}).inserted_id
    except errors.DuplicateKeyError:
          song_id=songs.find_one({"_id":track.id})
    except Exception as e:
          return {"status":"error","data":e}

    try:
        res=playlists.update_one({"_id":ObjectId(info.playlist_id)},{"$push":{"songs":song_id}})
        if res.modified_count>0 :
                    return {"status":"ok"}
        else:
                    return {"status":"error"}
    except Exception as e:
          return {"status":"error","data":e}
          


@user_router.post("/follow_playlist")
async def playlist_follow(follow_request:FollowPlaylist):
    #Follow a particular playlist
    try:
        
        res=users.update_one({"_id":follow_request.user_id},{"$push":{"following":follow_request.playlist_id}})
        print(res.modified_count)

    except Exception as E:
          print(E)
    return {"status":"Not implemented"}

@user_router.post("/delete_playlist")
async def user_playlist_delete(delete_playlist_request:DeletePlaylist):
    try:
            res=users.update_one({"_id":delete_playlist_request.user_id},{"$pull":{"following":delete_playlist_request.playlist_id}})
            if res.modified_count>0:
                  return {"status":"ok"}
            else:
                  return{"status":"error","data":"Not found"}
                  
    except Exception as E:
          print(E)
          return {"status":"error"}
    
