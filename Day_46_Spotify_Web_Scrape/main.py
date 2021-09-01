import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
from bs4 import BeautifulSoup
from pprint import pprint


SPOTIFY_CLIENT_ID = "your-spotify-client-id"
SPOTIFY_CLIENT_SECRET = "your-spotify-client-secret"

scope = "playlist-modify-private"
redirect_uri = "http://example.com"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET,scope=scope, redirect_uri=redirect_uri))

user_id = sp.current_user()["id"]
print(user_id)

date = input("Which year do you want to travel to? Type the date in this format: YYYY-MM-DD: ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
billboard_web_page = response.text

soup = BeautifulSoup(billboard_web_page, "html.parser")

song_titles = [song_tag.getText() for song_tag in soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")]
song_uris = []

for song_title in song_titles:
    result = sp.search(song_title)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song_title} doesn't exist in Spotify. Skipped.")
playlist_id = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)["id"]
sp.playlist_add_items(playlist_id, song_uris)
