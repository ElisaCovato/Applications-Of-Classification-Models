import os
import pickle

from parse_out_text import parse_email

"""
    Run this script to process the emails from Sara and Chris by extracting the words
    (features) and saving them in pickle files, ready to get vectorized and 
    used for the classification.
"""

from_sara = open("../data/from_sara.txt", "r")
from_chris = open("../data/from_chris.txt", "r")

# authors list
from_data = []
# words list
word_data = []

temp_counter = 0

print("Parsing out all emails...")
for name, from_person in [("sara", from_sara), ("chris", from_chris)]:
    for path in from_person:
        # Create path to go and fetch emails
        path = os.path.join('../data/', path[:-1])
        # print(path)

        # Open email
        email = open(path, "r")

        # Extract text from email
        text = parse_email(email)

        # Remove any instance of the words ["sara", "shackleton", "chris", "germani"]
        words_to_remove = ["sara", "shackleton", "chris", "germani", "sshacklensf", "cgermannsf"]
        for word in words_to_remove:
            text = text.replace(word, "")

        # Append the text to word_data
        word_data.append(text)

        # Append '0' to from_data if email is from Sara, and '1' id email is from Chris
        if name == 'sara':
            from_data.append(0)
        else:
            from_data.append(1)

        # Close the email
        email.close()

from_sara.close()
from_chris.close()
print("Emails processed!")


pickle.dump(word_data, open("../data/word_data.pkl", "wb"))
print("Words saved into pickle file")


pickle.dump(from_data, open("../data/email_authors.pkl", "wb"))
print("Email authors saved into pickle file")
