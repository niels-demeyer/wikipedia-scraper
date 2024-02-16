<p align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
</p>
<p align="center">
    <h1 align="center">WIKIPEDIA-SCRAPER</h1>
</p>
<p align="center">
    <em><code>► wikipedia-scraper</code></em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/last-commit/niels-demeyer/wikipedia-scraper?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/niels-demeyer/wikipedia-scraper?style=flat&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/niels-demeyer/wikipedia-scraper?style=flat&color=0080ff" alt="repo-language-count">
<p>
<hr>

##  Quick Links

> - [ Overview](#-overview)
> - [ Features](#-features)
> - [ Repository Structure](#-repository-structure)
> - [ Modules](#-modules)
> - [ Getting Started](#-getting-started)
>   - [ Installation](#-installation)
>   - [Running wikipedia-scraper](#-running-wikipedia-scraper)
> - [ Acknowledgments](#-acknowledgments)

---

##  Overview
This repository leverages the [this API](https://country-leaders.onrender.com/docs) to retrieve information about various country leaders. Subsequently, it employs BeautifulSoup to extract the first paragraph from each leader's Wikipedia page.


---

##  Features

This project was made during my time at BeCode and these where the requirements

| Criterion      | Indicator                                                    | Yes/No |
| -------------- | ------------------------------------------------------------ | ------ |
| 1. Is complete | Executes whithout errors                                     | Yes    |
|                | Stores the correct information from the API in the file      | Yes    |
| 2. Is correct  | The code is well typed                                       | Yes    |
|                | Good usage of OOP                                            | Yes    |
| 3. Is great    | Possibility to store output as a CSV file                    | Yes    |
|                | Correct usage of `Session()`                                 | Yes    |
|                | Multi-processing                                             | Yes    |

---

##  Repository Structure

```sh
└── wikipedia-scraper/
    ├── README.md
    ├── leaders.csv
    ├── leaders.json
    ├── main.py
    ├── requirements.txt
    ├── src
      └── scraper.py
```

---

##  Modules
- `requests`: This module allows you to send HTTP requests using Python. It abstracts the complexities of making requests behind a beautiful, simple API so that you can focus on interacting with services and consuming data in your application.

- `bs4 (BeautifulSoup)`: This library is used for web scraping purposes to pull the data out of HTML and XML files. It creates a parse tree from page source code that can be used to extract data in a hierarchical and more readable manner.

- `re`: This module provides regular expression matching operations similar to those found in Perl. It's used for string searching and manipulation.

- `json`: This module is used to work with JSON data in Python. It can parse JSON from strings or files and can convert objects into JSON strings.

- `typing`: This module provides support for type hints, a syntax for declaring the expected types of function arguments and return values.

- `concurrent.futures`: This module provides a high-level interface for asynchronously executing callables. The asynchronous execution can be performed with threads, using ThreadPoolExecutor, or separate processes, using ProcessPoolExecutor. Both implement the same interface, which is defined by the abstract Executor class.


| File                                                                                                | Summary                                                                                                                                                                                                                                                                                               |
| ---                                                                                                 | ---                                                                                                                                                                                                                                                                                                   |
| [requirements.txt](https://github.com/niels-demeyer/wikipedia-scraper/blob/master/requirements.txt) | Use this file to install the right dependencies.                     |
| [main.py](https://github.com/niels-demeyer/wikipedia-scraper/blob/master/main.py)                   | The `main.py` code in the `wikipedia-scraper` repository uses a `WikipediaScraper` class to fetch data about leaders from various countries. It then uses multi-threading to scrape the first paragraph of each leader's Wikipedia page. Finally, it saves the results to a JSON file and a CSV file. |                                |
| [leaders.json](https://github.com/niels-demeyer/wikipedia-scraper/blob/master/leaders.json)         | <code>► Result in json format></code>                                                                                                                                                                                                                                                               |
| [leaders.csv](https://github.com/niels-demeyer/wikipedia-scraper/blob/master/leaders.json)         | <code>► Result in csv format></code>                                                                                                                                                                                                                                                               |

</details>

<details closed><summary>src</summary>

| File                                                                                        | Summary                         |
| ---                                                                                         | ---                             |
| [scraper.py](https://github.com/niels-demeyer/wikipedia-scraper/blob/master/src/scraper.py) | <code>► Stores the `WikipediaScraper` class </code> |

</details>

---

##  Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* **Python**: `version 3.11.6`

###  Installation

1. Clone the wikipedia-scraper repository:

```sh
git clone https://github.com/niels-demeyer/wikipedia-scraper
```

2. Change to the project directory:

```sh
cd wikipedia-scraper
```

3. Install the dependencies:

```sh
pip install -r requirements.txt
```

###  Running `wikipedia-scraper`

Use the following command to run wikipedia-scraper:

```sh
python main.py
```

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/niels-demeyer/wikipedia-scraper/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/niels-demeyer/wikipedia-scraper/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/niels-demeyer/wikipedia-scraper/issues)**: Submit bugs found or log feature requests for the `wikipedia-scraper` project.

<details closed>
    <summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/niels-demeyer/wikipedia-scraper
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

</details>

---

##  Acknowledgments
This project was an asignment for the BeCode ai bootcamp.
