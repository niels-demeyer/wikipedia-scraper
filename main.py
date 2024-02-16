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
        """
        Creates a ThreadPoolExecutor with a maximum of 10 workers. This executor will be used to run multiple tasks concurrently.
        """
        for country, leaders in scraper.leaders_data.items():
            """
            Iterates over each country and its leaders in the leaders_data dictionary of the scraper object.
            For each leader of the current country, a new task is submitted to the executor.
            The task is to call the fetch_leader_data method of the scraper object with the leader as the argument.
            The submit method returns a Future object that represents the execution of the task.
            All the Future objects are stored in the futures list.
            The result of each Future (i.e., the return value of the fetch_leader_data method for each leader) is retrieved using the result method of the Future.
            These results are stored in the leaders_data dictionary of the scraper object, replacing the original list of leaders for the current country.
            """
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
