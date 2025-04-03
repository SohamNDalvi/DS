# Sample plays and words
plays = {
    "Play1": "Anthony is here, Brutus is here.",
    "Play2": "Caeser is here, but Calpurnia is not.",
    "Play3": "Cleopatra is here, mercy is here.",
}

# List of words to check in the plays
words = ["Anthony", "Brutus", "Caeser", "Calpurnia", "Cleopatra", "mercy"]

# Create a matrix to represent the presence of words in plays
mat = []
for word in words:
    row = []  # Initialize a new row for the current word
    for text in plays.values():
        # Check if the word is in the play's text and append 1 (true) or 0 (false)
        row.append(int(word in text))
    mat.append(row)  # Add the row to the matrix

# Display the presence matrix
print("Presence Matrix:")
for row in mat:
    print(row)

# Convert each row of the matrix to a binary string
vecd = []  # Initialize an empty list for binary strings
for row in mat:
    binary_string = ""  # Start with an empty string for the current row
    for x in row:
        binary_string += str(x)  # Append each element (0 or 1) to the string
    vecd.append(binary_string)  # Add the completed binary string to the list

# Display the binary representation of presence
print("Binary Representation of Presence:")
print(vecd)

# Input condition from the user
cond = input("Enter the condition (use 'and', 'or', 'not'): ")
cond_words = cond.split()  # Split the input into individual words

# Prepare to evaluate the condition
eval_cond = ""
for word in cond_words:
    if word in words:
        # If the word is in the list of words, find its index
        index = words.index(word)
        # Append the corresponding binary string to the evaluation condition
        eval_cond += vecd[index]
    elif word == "and":
        eval_cond += "&"  # Append the AND operator
    elif word == "or":
        eval_cond += "|"  # Append the OR operator
    elif word == "not":
        eval_cond += "~"  # Append the NOT operator

# Calculate the result of the logical expression
# Replace '~' with 'not' for Python evaluation
result = eval(eval_cond.replace("~", "not "))

# Determine which plays meet the condition
which_plays = []  # Initialize an empty list for plays that meet the condition
for i, play in enumerate(plays.keys()):
    # Check if the result for the current play is True (1)
    if result[i]:
        which_plays.append(play)  # Add the play to the list if it meets the condition

# Output the results
print("Plays that meet the condition:", which_plays)
