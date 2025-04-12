# Algorithm for Sentence Analysis.

# Initialize counters
length = 0       # Total number of characters (excluding the period)
word_count = 1   # Start at 1 assuming there is at least one word if sentence is not empty
vowel_count = 0

# Prompt user input for the sentence ending with a point
sentence = input("Enter a sentence ending with a point: ")

# Process each character until the period is encountered
for char in sentence:
    if char == '.':
        # Stop processing when we reach the period at the end
        break

    # Increment character counter
    length += 1

    # Check if the character is a vowel (case-insensitive)
    if char in "aeiouyAEIOUY":
        vowel_count += 1

    # Check for word separators (spaces)
    if char == ' ':
        word_count += 1

# Output the results
print("Length:", length)
print("Words:", word_count)
print("Vowels:", vowel_count)
