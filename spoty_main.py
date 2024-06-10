from requests import get
import random
from os import path
#from pygame import mixer
#import time
from spoty_functions import compute_energy, get_token, get_auth_header, get_features, search_for_song
import webbrowser
import json

client_id = "b3a47786876e4b3caf05c32b0bf2feea"
client_secret = "f7021e75f1144c0fa6ccade8bfbf8ce8"
query_limit = 10
path = "selectedSong.mp3"
song_name = "adieu tchami"


def spotify_search (song_name, client_id, client_secret, query_limit, path):
    
    token = get_token(client_id, client_secret)
    song_ids, song_urls = search_for_song(token, song_name, query_limit)
    random_num = random.randint(0, len(song_ids)-1)
    chosen_id = song_ids[random_num]
    features = get_features(token, chosen_id)
    
    
    download_url = song_urls[random_num]
    response = get(download_url)

    # Save as mp3 file
    with open(path, 'wb') as s:
        s.write(response.content)

    energy_data = compute_energy('selectedSong.mp3')
    '''
    y, sr = librosa.load("selectedSong.mp3")
    tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
    time_beats = librosa.frames_to_time(beats, sr=sr)
    
    features["first_beat"] = time_beats[0]
    features["bpm"] = tempo
    '''
    features["instant_energy"] = energy_data
    
    # Open the HTML file hosted on localhost !PAY ATTENTION TO THE PORT
    url = "http://localhost:8070/demo/index.html"
    json_object = json.dumps(features, indent=4)
    with open("song_parameters.json", "w") as outfile:
        outfile.write(json_object)

    #mixer.init()
    #mixer.music.load(path)
    #mixer.music.play()
    
    webbrowser.open(url)
    #while mixer.music.get_busy():  # wait for music to finish playing
    #    time.sleep(1)
 

spotify_search (song_name, client_id, client_secret, query_limit, path)

