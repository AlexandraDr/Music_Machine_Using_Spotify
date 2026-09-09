import os
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()
travel_date = input("Which year do you want to travel to? Type the date in this format: YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/{travel_date}"
headers = {
    "User-Agent": "USER_AGENT"
}

response = requests.get(URL, headers=headers)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
song_tags = soup.select("li ul li h3")

song_titles = [song.getText().strip() for song in song_tags]


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.environ["APP_CLIENT_ID"],
                                               client_secret=os.environ["APP_CLIENT_SECRET"],
                                               redirect_uri=os.environ["APP_REDIRECT_URI"],
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt",
                                               username=os.environ["SPOTIFY_USERNAME"]))
user_id = sp.current_user()["id"]


# Searching Spotify for songs by title
song_uris = []
year = travel_date.split("-")[0]

for song in song_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)

    except IndexError:
        print(f"{song} do not exist in Spotify. Skipped")

# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{travel_date} Billboard 100", public=False)


# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

print(playlist)
