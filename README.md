# Elternaccounts

Dieses Programm ist dafür gedacht das Erstellen von webuntis Elternaccounts möglichst zeiteffekt und sicher zu gestalten.

Die Eltern können über ein Nextcloud Formular ihre Daten eingeben. Anschließend werden die Angaben in eine Excel Tabelle übertragen. Dort können die Klassenlehrer die Daten überprüfen und ggf. korrigieren und das Programm überführt dann alle bestätigten Daten in ein für webuntis importierbares csv Format.

Es arbeitet mit dem output des Programms schild2keycloak, lässt sich aber auch einfach anpassen um mit anderen Datenquellen zu arbeiten.


## Voraussetzungen

Um dieses Projekt auszuführen, benötigen Sie:

- Python 3.7 oder höher
- Installierte Pakete aus der Datei `requirements.txt`

Führen Sie den folgenden Befehl aus, um alle erforderlichen Python-Pakete zu installieren:

```bash
pip install -r requirements.txt
```

## Verwendung

### Nextcloud Forms API

Die `NextcloudFormsAPI`-Klasse bietet Methoden zum Abrufen und Bearbeiten von Formularen und deren Einreichungen.

- **Initialisierung**

  ```python
  api = NextcloudFormsAPI(base_url='https://your-nextcloud-instance.com', username='deinBenutzername', password='deinPasswort')
  ```

- **Formulare abrufen**

  ```python
  response = api.get_forms()
  ```

- **Geteilte Formulare abrufen**

  ```python
  response = api.get_shared_forms()
  ```

- **Formulareinreichungen abrufen**

  ```python
  response = api.getFormSubmissions('formularHash')
  ```

### E-Mail-Operationen

Die Funktionen im Modul `email_operations.py` extrahieren E-Mail-Adressen und verwalten E-Mail-Nachrichten.

- **E-Mails extrahieren**

  ```python
  email_list = finde_email_adressen('Hier ist ein Text mit einer E-Mail-Adresse: test@example.com')
  ```

- **E-Mails senden**

  (Implementierung: Fügen Sie den Code in `sende_email` ein und nutzen Sie die Funktion entsprechend.)

### Dateioperationen

Das Modul `file_operations.py` enthält Funktionen zum Hoch- und Herunterladen von Dateien von und zu einem Server.

- **Datei herunterladen**

  ```python
  get_file(url='https://example.com/file', filename='lokaleDatei.txt', username='deinBenutzername', password='deinPasswort')
  ```

- **Datei hochladen**

  ```python
  put_file(url='https://example.com/target', filename='lokaleDatei.txt', username='deinBenutzername', password='deinPasswort')
  ```

## Verarbeitung von Daten

In `data_processing.py` sind Funktionen implementiert, die zur spezifischen Datenverarbeitung genutzt werden können. 

### Benutzername-Generierung

Im Modul `utils.py` wird basierend auf Vor- und Nachnamen ein Benutzername generiert:

- **Beispiel**

  ```python
  username = returnUsername(given='Max', last='Mustermann', typ='vorname.nachname')
  ```

## Beiträge und Weiterentwicklung

Beiträge zu diesem Projekt sind willkommen! Bitte senden Sie Pull-Requests oder öffnen Sie Issues, um Fehler zu melden oder neue Funktionen vorzuschlagen.

## Lizenz

Erstmal keine...

---

Weitere Informationen zum Projektablauf oder zur Beitragserstellung können im Main-Modul oder spezifischen Funktionsumsetzungen gefunden werden. Überprüfen Sie beispielsweise die Module `email_operations.py` oder `forms2.py` für detaillierte Implementierungen und erweiterbare Schnittstellen.

## Projektarchitektur

Das Projekt ist in mehrere Module unterteilt, die jeweils für spezifische Funktionalitäten verantwortlich sind:

- **forms2.py**: Verwaltet die Interaktionen mit der Nextcloud Forms API, einschließlich des Abrufens von Formularen und Einreichungen.

- **email_operations.py**: Bietet Funktionen zur Extraktion von E-Mail-Adressen und zum Versand von E-Mails.

- **file_operations.py**: Enthält Funktionen zum Hoch- und Herunterladen von Dateien über HTTP.

- **utils.py**: Stellt Hilfsfunktionen zur Verfügung, wie die Generierung von Benutzernamen und die Berechnung von String-Ähnlichkeiten.

- **data_processing.py**: Verarbeitet spezielle Datensätze und generiert Berichte oder Benutzerkonten basierend auf CSV-Dateien.

- **continue_tutorial.py**: Beinhaltet beispielhafte oder erweiterbare Funktionen wie Sortieralgorithmen.

- **main.py**: Der Einstiegspunkt der Anwendung, in dem die Hauptabläufe und Interaktionen gesteuert werden.

## Entwicklung

Beim Entwickeln mit diesem Projekt sollten Sie die modulare Struktur beachten und passende Tests für die jeweiligen Funktionen schreiben. Achten Sie darauf, das Logging zu verwenden, um den Anwendungsstatus zur Laufzeit zu verfolgen.

## Fehlersuche

Sollten Probleme oder unerwartete Verhaltensweisen auftreten:

- Validieren Sie die Konfigurationsdateien, insbesondere solche, die Zugangsdaten und API-URLs enthalten.
- Nutzen Sie das Logging, um mehr Informationen über die Anwendungsprozesse zu erhalten.
- Prüfen Sie externe Abhängigkeiten und deren Versionen, wie in `requirements.txt` spezifiziert.

## Lernen und Support

Für ein besseres Verständnis der verwendeten Bibliotheken und Methoden empfiehlt es sich:

- Die offizielle Dokumentation der verwendeten Python-Pakete zu konsultieren.
- Beispielanwendungen oder Tutorials zu Nextcloud API oder HTTP-Anfragen in Python zu studieren.
- Die README-Dateien und die im Projekt inkludierten spezifischen Dokumentationen zu nutzen.

Sollten weiterhin Fragen bestehen, eröffnen Sie ein Issue im Repository oder treten Sie mit dem Entwicklungsteam in Kontakt. Ihr Feedback und Ihre Beiträge sind wertvoll und helfen, das Projekt stetig zu verbessern.

---

Dieses README bietet einen umfassenden Überblick über den Projektumfang und die funktionalen Bestandteile. Bei Bedarf können Abschnitte weitervertieft oder spezifische Anwendungsfälle und Beispiele hinzugefügt werden.

