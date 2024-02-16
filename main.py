from concurrent.futures import ThreadPoolExecutor
from src.scraper import WikipediaScraper


def main():
    """
    Main function that orchestrates the scraping process.
    """
    scraper = WikipediaScraper()
    countries = scraper.get_countries()

    for country in countries:
        scraper.get_leaders(country)

    # use the wikipedia scraper to get the first paragraph of the wikipedia page for each leader
    with ThreadPoolExecutor(max_workers=10) as executor:
        for country, leaders in scraper.leaders_data.items():
            futures = [
                executor.submit(scraper.fetch_leader_data, leader) for leader in leaders
            ]
            scraper.leaders_data[country] = [future.result() for future in futures]

    # save the results to a json file and a csv file
    scraper.to_json_file("leaders.json")
    scraper.save_to_csv("leaders.csv")


if __name__ == "__main__":
    """
    Entry point of the script. Calls the main function.
    """
    main()
