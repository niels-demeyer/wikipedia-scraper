import requests
from bs4 import BeautifulSoup
import json


class WikipediaScraper:
    def __init__(self):
        self.base_url = "https://country-leaders.onrender.com"
        self.country_endpoint = "/countries"
        self.leaders_endpoint = "/leaders"
        self.cookies_endpoint = "/cookie"
        self.leaders_data = {}
        self.cookie = self.refresh_cookie()

    def refresh_cookie(self):
        response = requests.get(self.base_url + self.cookies_endpoint)
        return response.cookies

    def get_countries(self):
        response = requests.get(
            self.base_url + self.country_endpoint, cookies=self.cookie
        )
        return response.json()

    def get_leaders(self, country):
        response = requests.get(
            self.base_url + self.leaders_endpoint,
            params={"country": country},
            cookies=self.cookie,
        )
        self.leaders_data[country] = response.json()

    def get_first_paragraph(self, wikipedia_url):
        response = requests.get(wikipedia_url)
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all("p")

        for paragraph in paragraphs:
            if (
                len(paragraph.text) > 100
            ):  # You can adjust this value based on your needs
                return paragraph.text

        return None

    def to_json_file(self, filepath):
        with open(filepath, "w", encoding="utf-8") as json_file:
            json.dump(self.leaders_data, json_file, ensure_ascii=False)
