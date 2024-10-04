"""
utils.py

Dieses Modul enthält Hilfsfunktionen zur Verarbeitung von Zeichenfolgen, einschließlich:

1. Berechnung der Ähnlichkeit zwischen zwei Strings unter Verwendung des Levenshtein-Verhältnisses.
2. Generierung von Benutzernamen anhand von Vor- und Nachnamen, mit verschiedenen Formatoptionen.

Funktionen:
- similar(a: str, b: str) -> float: Berechnet die Ähnlichkeit zwischen zwei Zeichenfolgen.
- returnUsername(given: str, last: str, typ: str) -> str: Erstellt einen Benutzernamen basierend auf verschiedenen Formatoptionen.

Hinweis:
- Dieses Modul verwendet die `Levenshtein`-Bibliothek. Stellen Sie sicher, dass sie installiert ist.
"""
from Levenshtein import ratio
import mappings
import logging

logger = logging.getLogger(__name__)


def similar(a: str, b: str) -> float:
    """
    Berechnet die Ähnlichkeit zwischen zwei Strings anhand des Levenshtein-Verhältnisses.
    Der Levenshtein-Algorithmus bestimmt, wie ähnlich zwei Zeichenfolgen sind, basierend auf
    der Anzahl der Anpassungen (Einfügungen, Löschungen oder Ersetzungen), die erforderlich sind,
    um eine Zeichenfolge in die andere zu überführen. 

    Args:
        a (str): Der erste zu vergleichende String.
        b (str): Der zweite zu vergleichende String.

    Returns:
        float: Ein Wert zwischen 0 und 1, wobei 1 eine perfekte Übereinstimmung und 0 keine Ähnlichkeit darstellt.
    """
    return ratio(a.lower(), b.lower())


def returnUsername(given: str, last: str, typ: str) -> str:
    """
    Generiert einen Benutzernamen basierend auf dem Vor- und Nachnamen des Benutzers
    und der angegebenen Typformatierung. Es stehen zwei Typen zur Verfügung:
    'vorname.nachname' und 'kurzform'.

    - Bei 'vorname.nachname' wird der Benutzername im Format 'vorname.nachname' generiert.
      Der Vor- und Nachname werden mithilfe einer Zeichentabelle in mappings.mappingusername
      übersetzt, Leerzeichen und Bindestriche im Nachnamen entfernt.

    - Bei 'kurzform' wird ein kürzerer Benutzername generiert, der aus den ersten 4 Zeichen
      des Vornamens und den ersten 4 Zeichen des Nachnamens besteht, nach Anwendung der Zeichentabelle.

    Falls der generierte Benutzername in einer Liste alternativer Benutzernamen
    (mappings.alternative_usernames) enthalten ist, wird er durch einen alternativen
    Benutzernamen aus mappings.alt_usernames ersetzt.

    Args:
        given (str): Der Vorname des Benutzers.
        last (str): Der Nachname des Benutzers.
        typ (str): Der gewünschte Typ des Benutzernamensformats ('vorname.nachname' oder 'kurzform').

    Returns:
        str: Der generierte Benutzername in Kleinbuchstaben.
    """
    if typ == "vorname.nachname":
        username = (
            given.translate(mappings.mappingusername).split(" ")[0]
            + "."
            + last.translate(mappings.mappingusername).replace(" ", "").replace("-", "")
        )
        if username in mappings.alternative_usernames:
            username = mappings.alt_usernames.get(username, username)
    elif typ == "kurzform":
        username = (
            given.translate(mappings.mappingusername).split(" ")[0][:4]
            + last.translate(mappings.mappingusername)
            .replace(" ", "")
            .replace("-", "")[:4]
        )
    return username.lower()
