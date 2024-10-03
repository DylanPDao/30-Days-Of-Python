import json
from collections import Counter

# Function to find the most spoken languages
def most_spoken_languages(filename, top_n):
    # Read the JSON data
    with open(filename, 'r') as file:
        countries_data = json.load(file)
    
    # Extract languages from all countries
    languages = []
    for country in countries_data:
        languages.extend(country.get('languages', []))
    
    # Count occurrences of each language
    language_count = Counter(languages)
    
    # Sort by most common and return the top N languages
    return language_count.most_common(top_n)

# Example usage
print(most_spoken_languages(filename='./data/countries_data.json', top_m=10))
print(most_spoken_languages(filename='./data/countries_data.json', top_m=3))
