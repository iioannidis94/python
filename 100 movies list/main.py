import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


response = requests.get(URL)

web_resp = response.text
soup = BeautifulSoup(web_resp, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")
top_movies = [title.getText() for title in all_movies]
print(top_movies)
movies = top_movies[::-1]


with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")
