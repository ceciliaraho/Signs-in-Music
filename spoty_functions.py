import librosa
import numpy as np
import base64
import json
import librosa
import numpy as np
from requests import post, get
import math
import json

def gesture(message):
    songName = message
    return songName

def compute_energy(songUrl):
    song_signal, sampleRate = librosa.load(songUrl) #load song
    print(sampleRate)
    
    
    hop_length = 512
    frame_length = 512
    numberOfHops = len(song_signal)//hop_length 
    
    inst_energy = [] #create empty list
    padded_signal = np.pad(song_signal, (0, ((numberOfHops+1)*hop_length)-len(song_signal)), 'constant') #zero padding
    
    for i in range(numberOfHops-1):
        computed_energy = sum(abs((padded_signal[(i*hop_length):(i*hop_length+frame_length-1)])**2))
        inst_energy.append(math.floor(computed_energy))
    return inst_energy


#create valid token for a spotify request
def get_token(client_id, client_secret):
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"

    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

#create correct header for a specific token
def get_auth_header(token):
    return {"Authorization": "Bearer " + token}


def search_for_song(token, song_name, query_limit):
    #formulate request
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"q={song_name}&type=track&limit=" + str(query_limit)
    query_url = url + "?" + query
    #send request to spotify and store response
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)

    ids = []
    song_urls = []
    #take ids and urls of the found songs
    for i in range(query_limit):
        if json_result["tracks"]["items"][i]["preview_url"] != None: #some songs have as preview url 'None' -> in this case the song cannot be played 
            ids.append(json_result["tracks"]["items"][i]["id"])
            song_urls.append(json_result["tracks"]["items"][i]["preview_url"])
    
    print(len(ids))
    return ids, song_urls

def get_features(token, id):
    url="https://api.spotify.com/v1/audio-features/" + id
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_features = json.loads(result.content)
    print(json_features)
    return json_features


