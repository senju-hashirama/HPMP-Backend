def songs_serializer(song)->dict:
    return {
        "id": str(song["song_id"]),
        "title": str(song["title"]),
        "subtitle": str(song["subtitle"]),
        "song_url": str(song["song_url"]),
        "image_url": str(song["image_url"]),
        "artist_names":str(song["artist_names"]),
        "duration": str(song["duration"])
    }

def recently_played(songs):
    results=[]
    for i in songs:
        results.append(songs_serializer(i))
    return results

def playlist(playlist):
    return {
        "id": str(playlist["id"]),
        "title": str(playlist["title"]),
        "user_id": str(playlist["user_id"]),
        "songs": [songs_serializer(song) for song in playlist["songs"]],
        "view": int(playlist["view"]) 
    }
