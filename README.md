
# MITRE ATT&CK Scraper

This project provides tools to scrape and manage data from the MITRE ATT&CK framework, specifically designed to scrape, search, and display information about cyber threat groups listed on the MITRE ATT&CK website.

## Project Structure

```
mitre-attack-scraper/
│
├── .git/                  # Git repository files
├── .github/               # GitHub-specific files
│   └── workflows/         # GitHub Actions workflows
│       └── ci.yml         # Continuous integration setup
├── .gitignore             # Specifies intentionally untracked files to ignore
├── LICENSE                # The license for the project
├── README.md              # Project documentation
├── setup.py               # Setup script for the project installation
├── requirements.txt       # Python package dependencies
│
├── src/                   # Source code directory
│   ├── __init__.py        # Makes src a Python package
│   ├── scraper.py         # Scraper implementation
│   ├── search.py          # Search functionality
│   └── utils.py           # Utility functions
│
├── tests/                 # Unit tests directory
│   ├── __init__.py        # Makes tests a Python package
│   ├── test_scraper.py    # Test cases for the scraper
│   └── test_search.py     # Test cases for the search functionality
│
├── data/                  # Data files
│   ├── groups_info/       # Directory to store data.json
│   └── groups/            # Directory to store individual group data
├── docs/                  # Documentation files
|   ├── CODE_OF_CONDUCT.md       # Code of Conduct
|   ├── CONTRIBUTING.md          # Contributions
│   ├── DEVELOPER_GUIDE.md       # Installation guide
│   ├── INSTALLATION_GUIDE.md    # Installation guide
│   ├── RELEASE_NOTES.md         # Release notes 
│   ├── USER_GUIDE.md            # User guide
└── notebooks/             # Jupyter notebooks for exploration
```

## Installation

For detailed installation instructions, please see the [Installation Guide](docs/INSTALLATION_GUIDE.md).

## Usage

### Scraper

The `scraper.py` script is responsible for scraping the MITRE ATT&CK website and saving group data to a JSON file.

#### Usage

```bash
python src/scraper.py --output data/groups_info/data.json
```

#### Arguments

- `--output`: Specifies the file path to save the scraped data. Default is `data/groups_info/data.json`.

### Search

The `search.py` script provides functionality to search for group information based on ID, name, or associated groups. It also caches search results in `data/groups/{GROUPID}`.

#### Usage

- **Search by Name:**

  ```bash
  python src/search.py --name zirconium --input data/groups_info/data.json
  ```

- **Search by ID:**

  ```bash
  python src/search.py --id g0128 --input data/groups_info/data.json
  ```

- **Search by Associate:**

  ```bash
  python src/search.py --associate "Violet Typhoon" --input data/groups_info/data.json
  ```

#### Arguments

- `--name`: Search for a group by its name.
- `--id`: Search for a group by its ID.
- `--associate`: Search for all groups mentioning a specific associate.
- `--input`: Specifies the file path to read the group data. Default is `data/groups_info/data.json`.

### Utils

The `utils.py` script contains utility functions shared between the scraper and search scripts.

#### Functions

- **`load_groups_data(filepath)`**: Loads group data from a JSON file.
- **`display_group_info(group)`**: Displays information about a specific group in a formatted manner.
- **`cache_group_data(group, cache_dir)`**: Caches group data in a specified directory.

## Documentation

Detailed documentation can be found in the `docs` directory:

- [Installation Guide](docs/INSTALLATION_GUIDE.md)
- [User Guide](docs/USER_GUIDE.md)
- [Developer Guide](docs/DEVELOPER_GUIDE.md)
- [Release Notes](docs/RELEASE_NOTES.md)
- [Contributing](docs/CONTRIBUTING.md)
- [Code of Conduct](docs/CODE_OF_CONDUCT.MD)

## Data Structure

The data is stored in JSON format, with each group having the following structure:

```json
{
    "ID": "G0092",
    "Name": "TA505",
    "Associated Groups": "Hive0065, Spandex Tempest, CHIMBORAZO",
    "Description": "TA505 is a cyber criminal group that has been active since at least 2014. TA505 is known for frequently changing malware, driving global trends in criminal malware distribution, and ransomware campaigns involving Clop."
}
```

## Contributing

Contributions are welcome! Please read our [Developer Guide](docs/DEVELOPER_GUIDE.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

This project uses the MITRE ATT&CK framework. For more information, visit the [MITRE ATT&CK website](https://attack.mitre.org/).
