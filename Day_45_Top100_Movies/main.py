from bs4 import BeautifulSoup
import requests

response = requests.get("http://web.archive.org/web/20200518055830/https://www.empireonline.com/movies/features/best-movies-2/")
empire_web_page = response.text

soup = BeautifulSoup(empire_web_page, "html.parser")



movies = soup.find_all(name="h3", class_="title")

movie_titles = [movie.getText() for movie in movies[::-1]]

with open('movies.txt', "w") as file:
    for movie_title in movie_titles:
        file.write(f"{movie_title}\n")