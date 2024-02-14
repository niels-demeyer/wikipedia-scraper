from src.scraper import WikipediaScraper


# def main():
#     scraper = WikipediaScraper()
#     countries = scraper.get_countries()

#     for country in countries:
#         scraper.get_leaders(country)

#     scraper.to_json_file("leaders_data.json")


# if __name__ == "__main__":
#     main()


countries = WikipediaScraper().get_countries()
print(len(countries))
