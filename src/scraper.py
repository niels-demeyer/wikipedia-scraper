import requests
from bs4 import BeautifulSoup
import re
import json


class WikipediaScraper:
    def __init__(self):
        self.base_url = "https://country-leaders.onrender.com"
        self.country_endpoint = "/countries"
        self.leaders_endpoint = "/leaders"
        self.cookies_endpoint = "/cookie"
        self.leaders_data = {}
        self.session = requests.Session()
        self.refresh_cookie()

    def refresh_cookie(self):
        response = self.session.get(self.base_url + self.cookies_endpoint)

    def get_countries(self):
        response = self.session.get(self.base_url + self.country_endpoint)
        return response.json()

    def get_leaders(self, country):
        response = self.session.get(
            self.base_url + self.leaders_endpoint,
            params={"country": country},
        )
        self.leaders_data[country] = response.json()

    def get_first_paragraph(self, wikipedia_url):
        response = self.session.get(wikipedia_url)
        soup = BeautifulSoup(response.text, "html.parser")

        # Exclude paragraphs that are descendants of a div with class "bandeau-cell"
        paragraphs = [
            p
            for p in soup.find_all("p")
            if not p.find_parent("div", class_="bandeau-cell")
        ]

        for paragraph in paragraphs:
            if (
                len(paragraph.text) > 100
            ):  # You can adjust this value based on your needs
                return self.clean_text(paragraph.text)

        return None

    def clean_text(self, text):
        # Remove pronunciation
        text = re.sub(r"\(.*?\)", "", text)
        # Remove brackets and everything in brackets
        text = re.sub(r"\[.*?\]", "", text)
        # Remove \"
        text = re.sub(r"\"", "", text)
        # Remove pattern like [1]
        text = re.sub(r"\[\d+\]", "", text)
        # Remove specific string
        text = re.sub(
            r"Écouter\s*—\s*communément appelé\s*«\s*Giscard\s*»\s*ou désigné par ses initiales,\s*«\s*VGE\s*»\s*—,",
            "",
            text,
        )

        return text.strip()

    def to_json_file(self, filepath):
        with open(filepath, "w", encoding="utf-8") as json_file:
            json.dump(self.leaders_data, json_file, ensure_ascii=False)
