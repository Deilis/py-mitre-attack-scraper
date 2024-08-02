import requests
from bs4 import BeautifulSoup
import json
import os
import argparse

def fetch_groups_data(url):

    """Fetch the HTML content of given URL."""

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None

def parse_groups_data(html_content):

    """Parse the HTML content to extract group data."""

    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find('table', {'class': 'table-alternate'})
    if not table:
        print("Error: Could not find the groups table in the HTML content.")
        return []

    groups_data = []
    rows = table.find('tbody').find_all('tr')
    for row in rows:
        columns = row.find_all('td')
        if len(columns) < 4:
            continue

        group_id = columns[0].get_text(strip=True)
        name = columns[1].get_text(strip=True)
        associated_groups = columns[2].get_text(strip=True)
        description = columns[3].get_text(strip=True)

        group_info = {
            'ID': group_id,
            'Name': name,
            'Associated Groups': associated_groups,
            'Description': description
        }
        groups_data.append(group_info)

    return groups_data


def save_to_json(groups_data, filepath='data/groups_info/data.json'):

    """Save the extracted groups data to a JSON file."""

    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    with open(filepath, 'w') as json_file:
        json.dump(groups_data, json_file, indent=4)
    print(f"Data saved to [{filepath}].")

def main():
    # Argument Parser
    parser = argparse.ArgumentParser(description='Scrape MITRE ATT&CK group data and save it to a JSON file.')
    parser.add_argument(
        '--url',
        type=str,
        default='https://attack.mitre.org/groups/',
        help='URL of the MITRE ATT&CK groups page to scrape.'
    )
    parser.add_argument(
        '--output',
        type=str,
        default='data/groups_info/data.json',
        help='Output file path to save the scraped data.'
    )

    #Parse the arguments
    args = parser.parse_args()

    #Fetch and parse the data
    html_content = fetch_groups_data(args.url)
    if html_content:
        groups_data = parse_groups_data(html_content)
        save_to_json(groups_data, args.output)

if __name__ == '__main__':
    main()