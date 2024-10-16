
import requests
from bs4 import BeautifulSoup
import json

# URL of the page to scrape
url = 'http://www.bu.edu/president/boston-university-facts-stats/'

# Send a GET request to the webpage
response = requests.get(url)

# Parse the page content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Assuming we are looking for some specific sections of data, we will extract them
# Example: Extract all text from the content area (you can customize this to get specific stats or tables)
content = soup.find_all('div', class_='content-area')

# Extracting relevant text (you can extract more specific data based on the structure of the page)
data = [item.get_text(strip=True) for item in content]

# Save to JSON file
with open('bu_facts_stats.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print("BU Facts and Stats data saved to 'bu_facts_stats.json'")
