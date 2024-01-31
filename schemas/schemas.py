def songs_serializer(song)->dict:
    print(song)
    track={
        "title": str(song["title"]),
        "subtitle": str(song["subtitle"]),
        "song_url": str(song["song_url"]),
        "image_url": str(song["image_url"]),
        "artist_names":list(song["artist_names"]),
        "duration": str(song["duration"])
    }
    if "_id" in song:
        track["id"]=song["_id"]
    else:
        track["id"]=song["id"]
    return track

def recently_played(songs):
    results=[]
    for i in songs:
        
        results.append(songs_serializer(i))
    return results

def playlist(playlist)->dict:
    return {
        "id": str(playlist["_id"]),
        "title": str(playlist["title"]),
        "user_id": str(playlist["user_id"]),
        "songs": playlist["songs"],
        "image_url": str(playlist["image_url"]),
        "doc": str(playlist["doc"])
    }

def user_playlists(playlists):
    result=[]

    for i in playlists:
        
        result.append(playlist(i))
    print(result)
    return result
