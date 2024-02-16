0from concurrent.futures import ThreadPoolExecutor
from src.scraper import WikipediaScraper


def fetch_leader_data(scraper, leader):
    leader["wikipedia_first_paragraph"] = scraper.get_first_paragraph(
        leader["wikipedia_url"]
    )
    return leader


def main():
    scraper = WikipediaScraper()
    countries = scraper.get_countries()

    for country in countries:
        scraper.get_leaders(country)

    # use the wikipedia scraper to get the first paragraph of the wikipedia page for each leader
    with ThreadPoolExecutor(max_workers=10) as executor:
        for country, leaders in scraper.leaders_data.items():
            futures = [
                executor.submit(fetch_leader_data, scraper, leader)
                for leader in leaders
            ]
            scraper.leaders_data[country] = [future.result() for future in futures]

    # save the results to a json file
    scraper.to_json_file("leaders.json")
    scraper.save_to_csv("leaders.csv")


if __name__ == "__main__":
    main()

