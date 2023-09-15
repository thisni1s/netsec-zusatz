import sys
import hashlib
import requests
from dateutil.parser import parse

# Leet Speek substitutions dictionary
substitutions =  {
    'a': '4',
    'b': '8',
    'c': '<',
    'd': '|)',
    'e': '3',
    'f': '|=',
    'g': '6',
    'i': '1',
    'o': '0',
    'p': '|>',
    'q': '9',
    'r': '|2',
    's': '5',
    't': '7',
    'x': '><',
    'y': '`/',
    'z': '2'
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
    for letter, subs in substitutions.items():
        password_subs = password_subs.replace(letter, subs)        
    return check_password(password_subs)

def check_password(password):

    # Überprüfe ob das password aus dem Wörterbuch stammt (unabhängig von Groß/Kleinschreibung)
    if is_from_dictionary(password):
        print("Password is from the dictionary.")
        return False

    # Überprüfe ob das Passwort auf einer Liste steht die von Angreifern genutzt werden kann.
    if check_password_against_haveibeenpwned(password):
        print("Password is a common password used by attackers.")
        return False
    
    # Überprüfe auf Zahlenkombinationen die Daten ergeben.
    if is_date(password):
        print("Password is a date.")
        return False

    # Passwort hat alle Cheks bestanden
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
    print("Passwort ist sicher.")
