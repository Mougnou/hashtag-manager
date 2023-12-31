import re

def convert_to_hashtags(s):
    # Remove numbers that come after a colon
    s = re.sub(r':\s*\d*\.?\d+', '', s)
    # Remove all non-letter characters except comma and space
    s = re.sub(r'[^a-zA-Z0-9, ]', '', s)
    # Split the string into phrases by commas
    phrases = s.split(',')
    # Remove leading and trailing spaces from each phrase 
    hashtags = [phrase.strip() for phrase in phrases]
    # Join the phrases back together into a string with commas
    return ", ".join(hashtags)

