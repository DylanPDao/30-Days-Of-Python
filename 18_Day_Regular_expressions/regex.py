import re
from collections import Counter

# Given paragraph
paragraph = """I love teaching. If you do not love teaching what else can you love. 
I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love."""

# Use regular expressions to find all the words
words = re.findall(r'\b\w+\b', paragraph)

# Count the frequency of each word
word_count = Counter(words)

# Sort the word frequency in descending order and convert it to a list of tuples
sorted_word_count = sorted(word_count.items(), key=lambda item: item[1], reverse=True)

# Print the result
print(sorted_word_count)

import re

# Given text
text = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction."

# Extract all numbers (including negative ones) from the text using regular expressions
numbers = list(map(int, re.findall(r'-?\d+', text)))

# Find the distance between the two furthest particles
distance = max(numbers) - min(numbers)

# Print results
print("Extracted numbers:", numbers)
print("Distance between the two furthest particles:", distance)
