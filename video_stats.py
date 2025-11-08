import requests
import json  

API_KEY = 'AIzaSyD0kQKw_JqkaR8UyRW7q7ICywRSX4Arsc0'

CHANNEL_HANDLE = "MrBeast"

def get_playlist_Id():

    try: 

        url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}"

        response = requests.get(url)

        response.raise_for_status()

        print(response)

        data = response.json()

       # print(json.dumps(data,indent = 4))

        channel_items = data["items"][0]

        channel_playlistId = channel_items["contentDetails"]["relatedPlaylists"]['uploads']

        print(channel_playlistId)

        return channel_playlistId

    except requests.exceptions.RequestException as e: 
        raise e
    
if __name__ == '__main__': 
    #print("get_playlist_id will be executed")
    get_playlist_Id()
