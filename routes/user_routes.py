from fastapi import APIRouter,HTTPException,Request
from config.database import users,playlists,songs
from schemas.schemas import playlist, recently_played, user_playlists
from models.request_model import CreatePlaylist,Info,FollowPlaylist, DeletePlaylist,DeletePlaylistTrack,SetRecentlyPlayed
from helper.FirebaseAuth import Verify_Token
from pymongo import errors
from bson import ObjectId
user_router=APIRouter()





@user_router.get("/recently_played/{user_id}")
async def get_recebtly_played(user_id:str,request:Request):
    
    result=[]
    data=users.find_one({"_id":user_id})
    for i in data["recently_played"]:
          res=songs.find_one({"_id":i})
          result.append(res)
    return recently_played(result)

@user_router.get("/get_playlists/{user_id}")
async def get_user_playlists(user_id:str):
        p=playlists.find({"user_id":user_id})
        data=user_playlists(p)
        print("playlists",data)
        
        return {"status":"ok","data":data}
    


@user_router.get("/playlist_info/{pid}")
async def get_playlist_info(pid: str):
      res=playlists.find_one({"_id":ObjectId(pid)})
      
      if res:
            
            return {"status":"ok","data":playlist(res)}
      else:
            return {"status":"error","data":"Not Found"}

@user_router.post("/create_playlist")
async def playlist_create(playlist_info: CreatePlaylist,request: Request):
    
    userID=playlist_info.userid
    playlist=playlists.insert_one({"title":playlist_info.title,"user_id":playlist_info.userid,"songs":[],"image_url":playlist_info.image_url,"doc":playlist_info.doc})

    if playlist.inserted_id:
        res=users.update_one({"_id":playlist_info.userid},{"$push":{"playlists":playlist.inserted_id}})
        return {"status":"ok"}
    else:
        return {"status":"error"}

@user_router.post("/add_playlist_song")
async def update_playlist(info: Info):
    track=info.song_info
    
    try:
        song_id=songs.insert_one({"_id":track.id,"title":track.title,"song_url":track.song_url,"image_url":track.image_url,"artist_names":track.artist_names,"duration":track.duration,"subtitle":track.subtitle}).inserted_id
    except errors.DuplicateKeyError:
          song_id=songs.find_one({"_id":track.id})["_id"]
    except Exception as e:
          print(e)
          return {"status":"error","data":e}

    try:
        res=playlists.update_one({"$and":[{"_id":ObjectId(info.playlist_id)},{"user_id":info.user_id}]},{"$addToSet":{"songs":song_id}})
        if res.modified_count>0 :
                    return {"status":"ok"}
        else:
                    return {"status":"error","data":"Already exists"}
    except Exception as e:
          print(e)
          return {"status":"error","data":e}
          


# @user_router.post("/follow_playlist")
# async def playlist_follow(follow_request:FollowPlaylist):
#     #Follow a particular playlist
#     try:
        
#         res=users.update_one({"_id":follow_request.user_id},{"$push":{"following":follow_request.playlist_id}})
#         print(res.modified_count)

#     except Exception as E:Error: `'` can be escaped with `&apos;`, `&lsquo;`, `&#39;`, `&rsquo;`.  react/no-unescaped-entities
#           print(E)
#     return {"status":"Not implemented"}

@user_router.post("/delete_playlist")
async def user_playlist_delete(delete_playlist_request:DeletePlaylist):
    try:        
            res=playlists.delete_one({"$and":[{"_id":ObjectId(delete_playlist_request.playlist_id)},{"user_id":delete_playlist_request.user_id}]})
            return {"status":"ok"}
    except Exception as E:
          print(E)
          return {"status":"error"}

@user_router.post("/delete_playlist_track")
async def delete_playlist_track(delete_track:DeletePlaylistTrack):
      res=playlists.update_one({"$and":[{"_id":ObjectId(delete_track.playlist_id)},{"user_id":delete_track.user_id}]},{"$pull":{"songs":delete_track.song_id}})
      if res.modified_count>0:
            return {"status":"ok"}
      else:
            return {"status":"error"}
@user_router.post("/set_played")
async def set_recently_played(track: SetRecentlyPlayed ):
    
    try:
        song_id=songs.insert_one({"_id":track.song.id,"title":track.song.title,"song_url":track.song.song_url,"image_url":track.song.image_url,"artist_names":track.song.artist_names,"duration":track.song.duration,"subtitle":track.song.subtitle}).inserted_id
    except errors.DuplicateKeyError:
          song_id=track.song.id
    except Exception as e:
          print("yup")
          return {"status":"error","data":e}
    res=users.update_one({"_id":track.user_id},{"$addToSet":{"recently_played":song_id}})
    if res.modified_count>0:
          return {"status":"ok"}
    else:
          return {"status":"error","data":"error"}