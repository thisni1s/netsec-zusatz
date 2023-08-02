import sys
import hashlib
import requests
from dateutil.parser import parse

# Leet Speek substitutions dictionary
substitutions =  {
    '4': 'a',
    '@': 'a',
    '8': 'b',
    '(': 'c',
    '{': 'c',
    '3': 'e',
    '6': 'g',
    '9': 'g',
    '#': 'h',
    '1': 'l',
    '|': 'l',
    '0': 'o',
    '$': 's',
    '5': 's',
    '+': 't',
    '7': 't',
    '2': 'z',
    '!': 'i',
    '|': 'i'
}


def check_password_against_haveibeenpwned(password):
    sha1_password_hash = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix = sha1_password_hash[:5]

    url = f'https://api.pwnedpasswords.com/range/{prefix}'
    response = requests.get(url)

    if response.status_code == 200:
        res = response.text.splitlines()
        suffixes = [item[:35] for item in res]
        if sha1_password_hash[5:] in suffixes:
            return True
    return False

def is_date(string):
    try: 
        parse(string, fuzzy=True)
        return True
    except ValueError:
        return False
    
def is_from_dictionary(password) -> bool:
    with open("wordlist-german.txt", "r") as f:
        dictionary_words = [word.strip().lower() for word in f]
        if password.lower() in dictionary_words:
            return True
        else:
            return False
    
def check_with_substitutions(password) -> bool:
    password_subs = password
    for subs, letter in substitutions.items():
        password_subs = password_subs.replace(letter, subs)        
    return check_password(password_subs)

def check_password(password):

    # Check if the password is from a dictionary (case-insensitive)
    if is_from_dictionary(password):
        print("Password is from the dictionary.")
        return False

    # Check if the password is on the list of common passwords tried by attackers
    if check_password_against_haveibeenpwned(password):
        print("Password is a common password used by attackers.")
        return False
    
    # Check for combinations of numbers that are dates
    if is_date(password):
        print("Password is a date.")
        return False

    # Password passed all checks
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python password_checker.py <password>")
        sys.exit(1)

    password = sys.argv[1]
    
    if check_password(password) is False:
        sys.exit(1)
    if check_with_substitutions(password) is False:
        sys.exit(1)
    print("Password is secure.")
