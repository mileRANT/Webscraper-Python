import requests
from bs4 import BeautifulSoup

URL = "https://myanimelist.net/anime/season"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

animes_season = soup.find_all(name="h2", class_="h2_anime_title")

anime_titles = [anime.getText() for anime in animes_season]
animes = anime_titles[::-1]

with open("anime.txt", mode="w", encoding='utf-8') as file:
    for anime in animes:
        file.write(f"{anime}\n")

