import requests
from collections import Counter
import re

# URL for the text file of Romeo and Juliet
url = 'http://www.gutenberg.org/files/1112/1112.txt'

# Fetch the content of the text file
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Extract the text content
    text = response.text
    
    # Clean the text by removing non-alphabetic characters and converting it to lowercase
    words = re.findall(r'\b[a-z]+\b', text.lower())
    
    # Count the frequency of each word
    word_counts = Counter(words)
    
    # Find the 10 most common words
    most_common_words = word_counts.most_common(10)
    
    # Print the 10 most frequent words
    print("The 10 most frequent words are:")
    for word, count in most_common_words:
        print(f"{word}: {count}")
else:
    print("Failed to fetch the text.")
