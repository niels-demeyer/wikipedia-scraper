# wikipedia-scraper

This project is a Python-based web scraper that fetches data from a website that lists country leaders. The data is then enriched with the first paragraph of the leader's Wikipedia page.
It uses data from the following api: https://country-leaders.onrender.com/docs

### Files

src/scraper.py
This file contains the WikipediaScraper class which is responsible for all the scraping tasks. The class has the following methods:

**init**: Initializes the scraper with the base URL and endpoints for countries, leaders, and cookies. It also sets up a requests session and refreshes the cookie.

refresh_cookie: Refreshes the cookie for the session.

get_countries: Fetches a list of countries from the base URL.

get_leaders: Fetches the leaders for a given country and stores the data in a dictionary.

get_first_paragraph: Fetches the first paragraph of a given Wikipedia URL.

clean_text: Cleans the text fetched from the Wikipedia page by removing unnecessary characters and patterns.

to_json_file: Writes the leaders data to a JSON file.

### main.py

This file contains the main execution logic for the scraper. It creates an instance of WikipediaScraper, fetches the countries and their leaders, enriches the leaders' data with the first paragraph from their Wikipedia page, and finally writes the data to a JSON file and a csv file.

### Output

The output of this project is a JSON file named leaders.json and a csv file leaders.csv which contains the data of the leaders for each country, enriched with the first paragraph from their Wikipedia page.
