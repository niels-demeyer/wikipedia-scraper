import requests
from bs4 import BeautifulSoup
import re
import json
from typing import Optional, Dict, Any


class WikipediaScraper:
    """
    A class used to scrape data from Wikipedia.

    ...

    Attributes
    ----------
    base_url : str
        The base URL for the scraping.
    country_endpoint : str
        The endpoint for getting country data.
    leaders_endpoint : str
        The endpoint for getting leaders data.
    cookies_endpoint : str
        The endpoint for refreshing cookies.
    leaders_data : Dict[str, Any]
        A dictionary to store the leaders data.
    session : requests.Session
        A Session object to manage HTTP requests.

    Methods
    -------
    refresh_cookie():
        Refreshes the cookies for the session.
    get_countries() -> Dict[str, Any]:
        Gets the list of countries.
    get_leaders(country: str):
        Gets the leaders of a specific country.
    get_first_paragraph(wikipedia_url: str) -> Optional[str]:
        Gets the first paragraph of a Wikipedia page.
    fetch_leader_data(leader: Dict[str, Any]) -> Dict[str, Any]:
        Fetches the first paragraph of the Wikipedia page for a given leader.
    clean_text(text: str) -> str:
        Cleans the text by removing unwanted characters and patterns.
    to_json_file(filepath: str):
        Saves the leaders data to a JSON file.
    save_to_csv(filepath: str):
        Saves the leaders data to a CSV file.
    """

    def __init__(self):
        """Initializes the WikipediaScraper with the necessary endpoints and creates a new Session."""
        self.base_url: str = "https://country-leaders.onrender.com"
        self.country_endpoint: str = "/countries"
        self.leaders_endpoint: str = "/leaders"
        self.cookies_endpoint: str = "/cookie"
        self.leaders_data: Dict[str, Any] = {}
        self.session: requests.Session = requests.Session()
        self.refresh_cookie()

    def refresh_cookie(self) -> None:
        """Refreshes the cookies for the session."""
        response: requests.Response = self.session.get(
            self.base_url + self.cookies_endpoint
        )

    def get_countries(self) -> Dict[str, Any]:
        """Gets the list of countries from the country endpoint and returns it as a dictionary."""
        response: requests.Response = self.session.get(
            self.base_url + self.country_endpoint
        )
        return response.json()

    def get_leaders(self, country: str) -> None:
        """Gets the leaders of a specific country and stores them in the leaders_data dictionary."""
        response: requests.Response = self.session.get(
            self.base_url + self.leaders_endpoint,
            params={"country": country},
        )
        self.leaders_data[country] = response.json()

    def get_first_paragraph(self, wikipedia_url: str) -> Optional[str]:
        """
        Gets the first paragraph of a Wikipedia page.

        Parameters:
        wikipedia_url (str): The URL of the Wikipedia page.

        Returns:
        Optional[str]: The first paragraph of the Wikipedia page, or None if no suitable paragraph is found.
        """
        ...
        response: requests.Response = self.session.get(wikipedia_url)
        soup: BeautifulSoup = BeautifulSoup(response.text, "html.parser")

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

    def fetch_leader_data(self, leader: Dict[str, Any]) -> Dict[str, Any]:
        """
        Fetches the first paragraph of the Wikipedia page for a given leader.

        Parameters:
        leader (dict): The leader data.

        Returns:
        dict: The updated leader data with the first paragraph of the Wikipedia page.
        """
        leader["wikipedia_first_paragraph"] = self.get_first_paragraph(
            leader["wikipedia_url"]
        )
        return leader

    def clean_text(self, text: str) -> str:
        """
        Cleans the text by removing unwanted characters and patterns.

        Parameters:
        text (str): The text to clean.

        Returns:
        str: The cleaned text.
        """
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

    def to_json_file(self, filepath: str) -> None:
        """
        Saves the leaders data to a JSON file.

        Parameters:
        filepath (str): The path to the JSON file.
        """
        with open(filepath, "w", encoding="utf-8") as json_file:
            json.dump(self.leaders_data, json_file, ensure_ascii=False)

    def save_to_csv(self, filepath: str) -> None:
        """
        Saves the leaders data to a CSV file.

        Parameters:
        filepath (str): The path to the CSV file.
        """
        with open(filepath, "w", encoding="utf-8") as csv_file:
            csv_file.write(
                "country,id,first_name,last_name,birth_date,death_date,place_of_birth,wikipedia_url,start_mandate,end_mandate,wikipedia_first_paragraph\n"
            )
            for country, leaders in self.leaders_data.items():
                for leader in leaders:
                    csv_file.write(
                        f"{country},{leader['id']},{leader['first_name']},{leader['last_name']},{leader['birth_date']},{leader['death_date']},{leader['place_of_birth']},{leader['wikipedia_url']},{leader['start_mandate']},{leader['end_mandate']},\"{leader['wikipedia_first_paragraph']}\"\n"
                    )
