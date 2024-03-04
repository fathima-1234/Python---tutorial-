def contains_vowel(key):
    # Check if the key contains any vowels
    return any(char.lower() in 'aeiou' for char in key)

def remove_entries_with_vowel(dictionary):
    # Create a new dictionary with entries that don't have keys containing vowels
    result_dict = {key: value for key, value in dictionary.items() if not contains_vowel(key)}
    return result_dict

# Example dictionary
my_dict = {
    'apple': 5,
    'banana': 10,
    'grape': 7,
    'kiwi': 3,
    'orange': 8
}

# Remove entries with keys containing vowels
filtered_dict = remove_entries_with_vowel(my_dict)

# Print the result
print("Original Dictionary:", my_dict)
print("Filtered Dictionary:", filtered_dict)
