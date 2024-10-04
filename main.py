"""
main.py

This script performs various operations related to updating files, scraping emails, and processing email communication
for a system managing Elternaccounts (parent accounts). It offers three main options:

1. Update files with new data by downloading, processing, and uploading the necessary files.
2. Scrape email addresses from provided data and output them.
3. Scrape email addresses and send emails to the extracted addresses.

The script requires credentials and configuration details, which are imported from the elternaccounts_credentials
module. The operations involve interaction with Nextcloud for file handling, and the use of specified email
operations for handling email tasks.
"""
import logging
from file_operations import get_file, put_file
from data_processing import update_xlsx, createElternaccounts
from email_operations import finde_email_adressen, sende_email
import elternaccounts_credentials
from forms2 import NextcloudFormsAPI

# Logging konfigurieren
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s:%(name)s:%(message)s",
    handlers=[logging.FileHandler("app.log"), logging.StreamHandler()],
)

logger = logging.getLogger(__name__)


def main():
    while True:
        # Benutzer wird aufgefordert, eine Option zu wählen
        user_choice = input(
            """Wählen Sie eine Option (1, 2, 3):
1: Nur files aktualisieren.
2: Nur mails scrapen und Adressen ausgeben.
3: Mails scrapen und Mails verschicken.
"""
        )
        if user_choice == "1":
            exportfile = "00-Export20240929.csv"
            # API initialisieren
            ncapi = NextcloudFormsAPI(
                elternaccounts_credentials.server_url,
                elternaccounts_credentials.username,
                elternaccounts_credentials.password,
            )
            # forms.csv herunterladen
            file_content = ncapi.getFormSubmissionsCSV(
                elternaccounts_credentials.elternaccounts
            ).content
            with open("testforms.csv", "wb") as file:
                file.write(file_content)
            logger.info("Forms CSV-Datei wurde gespeichert")
            # xlsx herunterladen
            get_file(
                elternaccounts_credentials.url_elternaccounts_share,
                "testxlsx.xlsx",
                elternaccounts_credentials.username,
                elternaccounts_credentials.password,
            )
            # xlsx mit den neuen csv-Daten aktualisieren
            update_xlsx("testforms.csv", "testxlsx.xlsx")
            # xlsx wieder hochladen
            put_file(
                elternaccounts_credentials.url_elternaccounts_backup,
                "testxlsx.xlsx",
                elternaccounts_credentials.username,
                elternaccounts_credentials.password,
            )
            put_file(
                elternaccounts_credentials.url_elternaccounts_share,
                "testxlsx.xlsx",
                elternaccounts_credentials.username,
                elternaccounts_credentials.password,
            )
            # Aktuellste Schülertaten herunterladen
            get_file(
                f"{elternaccounts_credentials.url_export}{exportfile}",
                exportfile,
                elternaccounts_credentials.username,
                elternaccounts_credentials.password,
            )
            # CSV zum Erstellen der Elternaccounts in WebUntis erstellen
            createElternaccounts(
                "testxlsx.xlsx",
                exportfile,
                "elternaccounts-control.csv",
                "elternaccounts.csv",
            )
            # CSV hochladen
            put_file(
                elternaccounts_credentials.url_elterncsv,
                "elternaccounts.csv",
                elternaccounts_credentials.username,
                elternaccounts_credentials.password,
            )
            put_file(
                elternaccounts_credentials.url_elterncsvcontrol,
                "elternaccounts-control.csv",
                elternaccounts_credentials.username,
                elternaccounts_credentials.password,
            )
            break

        elif user_choice == "2":
            # Mailversand vorbereiten
            betreff = "WebUntis-Elternaccounts wurden erstellt. (Anleitung beachten!)"
            nachricht = elternaccounts_credentials.mailtext

            # Hier die vorher extrahierte E-Mail-Liste einfügen
            empfaenger_liste = finde_email_adressen(
                """
HIER DEN OUTPUT NACH DEM ERSTELLEN DER ACCOUNTS EINFÜGEN
              """
            )
            for name in set(empfaenger_liste):
                logger.info(f"Gefundene E-Mail-Adresse: {name}")
            logger.info(f"Anzahl der Empfänger: {len(set(empfaenger_liste))}")

            break

        elif user_choice == "3":
            # Mailversand durchführen
            betreff = (
                "WebUntis-Elternaccounts wurden erstellt, bitte der Anleitung folgen!"
            )
            nachricht = elternaccounts_credentials.mailtext

            # Hier die vorher extrahierte E-Mail-Liste einfügen
            empfaenger_liste = finde_email_adressen(
                """
HIER DEN OUTPUT NACH DEM ERSTELLEN DER ACCOUNTS EINFÜGEN
Rosa Medina rosemedinam@gmail.com Zarauz Rosa rosamedi
Wiebke Windorf wiebke@windorf.club Windorf Hugo weilwind
              """
            )
            logger.info(f"Empfänger-Liste: {empfaenger_liste}")
            logger.info(f"Anzahl der Empfänger: {len(empfaenger_liste)}")
            ergebnis = sende_email(
                empfaenger_liste,
                betreff,
                nachricht,
                elternaccounts_credentials.smtp_server,
                elternaccounts_credentials.smtp_port,
                elternaccounts_credentials.mail_benutzername,
                elternaccounts_credentials.mail_passwort,
            )
            logger.info(ergebnis)
            break

        else:
            logger.warning("Ungültige Eingabe. Bitte wählen Sie 1, 2 oder 3.")


if __name__ == "__main__":
    main()
