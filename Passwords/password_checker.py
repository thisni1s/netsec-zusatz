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

def check_password_against_haveibeenpwned(password) -> bool:
    #
    # TODO: Schicken sie das gehashte an haveibeenpwned und überprüfen sie,
    # ob das passwort in der liste der geknackten Passwörter steht. 
    #
    return False

def is_date(password) -> bool:
    #
    # TODO: Überprüfen sie ob das Passwort ein Datum enthält.
    # Tipp: Nutzen sie das Flag 'fuzzy' aus der dateutil library,
    # auch wenn diese sehr empfindlich ist, soll es hier ausreichen.
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
    # und prüfen sie dass dadurch enstandene Passwort
    # Es reicht aus wenn Sie einmal alle Buchstaben durch ihr LeetSpeak äquivalent ersetzen,
    # auch wenn in der Realität verschiedene Kombinationen möglich sind.
    #
    return 

def check_password(password):

    # Überprüfe ob das password aus dem Wörterbuch stammt (unabhängig von Groß/Kleinschreibung)
    if is_from_dictionary(password):
        print("Passwort stammt aus dem Wörterbuch")
        return False

    # Überprüfe ob das Passwort auf einer Liste steht die von Angreifern genutzt werden kann.
    if check_password_against_haveibeenpwned(password):
        print("Passwort steht auf einer Liste steht die von Angreifern genutzt werden kann. ")
        return False
    
    # Überprüfe auf Zahlenkombinationen die Daten ergeben.
    if is_date(password):
        print("Passwort enthält ein Datum")
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
