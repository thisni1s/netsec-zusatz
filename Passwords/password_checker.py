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


def check_password_against_haveibeenpwned(password) -> bool:
    #
    # TODO: Schicken sie das gehashte an haveibeenpwned und überprüfen sie,
    # ob das passwort in der liste der geknackten Passwörter steht. 
    #
    return False

def is_date(password) -> bool:
    #
    # TODO: Überprüfen sie ob das Passwort ein Datum enthält.
    # Tipp: Nutzen sie das Flag 'fuzzy' aus der dateutil library
    #
    return False

def is_from_dictionary(password) -> bool:
    #
    # TODO: Überprüfen sie ob das Passwort ein Wort aus dem Wörterbuch ist.
    # Nutzen sie dafür die Datei 'wordlist-german.txt' 
    #
    return False

def check_with_substitutions(password) -> bool:
    #
    # TODO: Ersetzen sie gängige LeetSpeak Zeichen durch normale Textzeichen
    # und prüfen sie dass dadurch enstandenen Passwort
    return 

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
