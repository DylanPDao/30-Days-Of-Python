# mymodule.py file
def generate_full_name(firstname, lastname):
    return firstname + ' ' + lastname

import random
import string

def generate_random_user_id():
    # Define the characters to choose from: digits and letters (uppercase + lowercase)
    characters = string.ascii_letters + string.digits
    # Randomly select six characters
    random_user_id = ''.join(random.choices(characters, k=6))
    return random_user_id

# Example usage:
print(generate_random_user_id())

def user_id_gen_by_user():
    # Take input for the number of characters in the user ID
    num_chars = int(input("Enter the number of characters for the user ID: "))
    # Take input for the number of IDs to be generated
    num_ids = int(input("Enter the number of user IDs to generate: "))
    
    # Define the characters to choose from: digits and letters (uppercase + lowercase)
    characters = string.ascii_letters + string.digits

    # Generate the required number of IDs
    ids = [''.join(random.choices(characters, k=num_chars)) for _ in range(num_ids)]

    # Return or print the list of generated IDs
    return ids

# Example usage:
generated_ids = user_id_gen_by_user()
for i, user_id in enumerate(generated_ids, 1):
    print(f"User ID {i}: {user_id}")
