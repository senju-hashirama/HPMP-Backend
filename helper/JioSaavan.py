from pyDes import *
import requests
import base64
from schemas import schemas


des_cipher = des(b"38346591", ECB, b"\0\0\0\0\0\0\0\0" , pad=None, padmode=PAD_PKCS5)
base_url = 'http://h.saavncdn.com'

def decrypt_url(url):
    enc_url = base64.b64decode(url.strip())
    dec_url = des_cipher.decrypt(enc_url,padmode=PAD_PKCS5).decode('utf-8')
    dec_url = base_url + dec_url.replace('mp3:audios','')
    return dec_url[21:]



def search(query: str, type: str=""):
    r=requests.get("https://www.jiosaavn.com/api.php?p=1&q={}&_format=json&_marker=0&api_version=4&ctx=wap6dot0&n=20&__call=search.getResults" .format(query))

    data=r.json()["results"]
    output=[]
    for results in data:
        output.append(
        schemas.songs_serializer({
        "song_id": results["id"],
        "title":results["title"].strip(),
        "subtitle":results["subtitle"].strip(),
        "image_url":results["image"].strip(),
        "duration":results["more_info"]["duration"].strip(),
        "song_url":decrypt_url(results["more_info"]["encrypted_media_url"]).strip(),
        "artist_names":[[j["name"].strip(),j["image"]] for j in results["more_info"]["artistMap"]["primary_artists"]]
        }))
    return output


if __name__=="__main__":
    print(search(type="",query="Bad Guy"))
