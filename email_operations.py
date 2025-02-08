"""
email_operations.py

This module provides functions to perform operations related to sending and retrieving emails.
It includes functionality to:
- Extract email addresses from a given text.
- Send emails to a specified list of recipients using SMTP.
- Store sent emails in the 'Sent' folder using IMAP.
- Retrieve the content of the 'Sent' folder from an IMAP account.

Modules used:
- smtplib for sending emails,
- imaplib for interacting with an IMAP server,
- email for handling email message content and structures.

Configuration, such as server addresses and credentials, is expected to be managed externally,
for example, in a separate credential module.

Functions:
- finde_email_adressen(text: str) -> list
- sende_email(empfaenger_liste: list, betreff: str, nachricht: str, smtp_server: str, smtp_port: int, benutzername: str, passwort: str) -> str
- get_sent_folder_content(imap_server: str, imap_port: int, benutzername: str, passwort: str) -> list
"""
import smtplib
import imaplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import decode_header
import time
import re
import elternaccounts_credentials
import logging

logger = logging.getLogger(__name__)


def finde_email_adressen(text: str) -> list:
    """
    Extracts all email addresses from a given text.

    Args:
        text (str): The text from which to extract email addresses.

    Returns:
        list: A list of found email addresses.
    """
    # Regular expression pattern for matching email addresses
    muster = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    # Find all matches in the text using the regular expression
    email_adressen = re.findall(muster, text)
    return email_adressen


def sende_email(
    empfaenger_liste: list = None,
    betreff: str = None,
    nachricht: str = None,
    smtp_server: str = None,
    smtp_port: int = None,
    benutzername: str = None,
    passwort: str = None,
    bcc: list = None,
    cc: list = None
) -> str:
    """
    Sends an email to recipients and stores it in the 'Sent' folder.

    Args:
        empfaenger_liste (list, optional): List of recipient email addresses or single recipient.
        betreff (str, optional): Subject of the email. Defaults to None.
        nachricht (str, optional): Body content of the email. Defaults to None.
        smtp_server (str, optional): SMTP server address. Defaults to credentials.
        smtp_port (int, optional): SMTP server port. Defaults to credentials.
        benutzername (str, optional): SMTP username. Defaults to credentials.
        passwort (str, optional): SMTP password. Defaults to credentials.
        bcc (list, optional): List of BCC recipients. Defaults to None.
        cc (list, optional): List of CC recipients. Defaults to None.

    Returns:
        str: Result of the email sending operation.
    """
    # Use credential defaults if not specified
    smtp_server = smtp_server or elternaccounts_credentials.smtp_server
    smtp_port = smtp_port or elternaccounts_credentials.smtp_port
    benutzername = benutzername or elternaccounts_credentials.mail_benutzername
    passwort = passwort or elternaccounts_credentials.mail_passwort

    # Handle single recipient or list
    if isinstance(empfaenger_liste, str):
        empfaenger_liste = [empfaenger_liste]
    
    if not empfaenger_liste and not bcc:
        return "Keine Empfängeradresse vorhanden."

    msg = MIMEMultipart()
    msg["From"] = benutzername
    
    # Handle To field
    if empfaenger_liste:
        msg["To"] = ", ".join(empfaenger_liste)
    else:
        msg["To"] = benutzername  # Send to self if only BCC
        
    # Handle BCC field
    if bcc:
        msg["Bcc"] = ", ".join(bcc)
        
    # Handle CC field
    if cc:
        msg["Cc"] = ", ".join(cc)
        
    if betreff:
        msg["Subject"] = betreff

    if nachricht:
        msg.attach(MIMEText(nachricht, "plain"))

    try:
        # Verbindung zum SMTP-Server mit SSL
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(benutzername, passwort)

        # E-Mail senden
        server.send_message(msg)
        server.quit()

        # Verbindung zum IMAP-Server herstellen
        mail = imaplib.IMAP4_SSL(
            elternaccounts_credentials.imap_server, elternaccounts_credentials.imap_port
        )
        mail.login(benutzername, passwort)
        mail.select('"Gesendet"')  # Für Gmail spezifisch

        # E-Mail im Gesendet-Ordner speichern
        result = mail.append(
            '"Gesendet"',
            "",
            imaplib.Time2Internaldate(time.time()),
            str(msg).encode("utf-8"),
        )
        mail.logout()

        if result[0] == "OK":
            return "E-Mail erfolgreich gesendet und im Gesendet-Ordner gespeichert."
        else:
            return "E-Mail gesendet, aber Fehler beim Speichern im Gesendet-Ordner."

    except Exception as e:
        return f"Fehler beim Senden der E-Mail: {e}"


def get_sent_folder_content(
    imap_server: str, imap_port: int, benutzername: str, passwort: str
) -> list:
    """
    Retrieves the content of the 'Sent' folder of an IMAP account.

    Args:
        imap_server (str): IMAP server address.
        imap_port (int): IMAP server port.
        benutzername (str): IMAP username for authentication.
        passwort (str): IMAP password for authentication.

    Returns:
        list: A list of emails in the 'Sent' folder.
    """
    try:
        mail = imaplib.IMAP4_SSL(imap_server, imap_port)
        mail.login(benutzername, passwort)
        mail.select('"Gesendet"')  # Für Gmail spezifisch

        status, messages = mail.search(None, "ALL")
        if status != "OK":
            return ["Fehler beim Abrufen der E-Mails."]

        email_ids = messages[0].split()
        emails_content = []

        for e_id in email_ids:
            status, msg_data = mail.fetch(e_id, "(RFC822)")
            if status != "OK":
                return [f"Fehler beim Abrufen der E-Mail mit ID {e_id.decode()}."]
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    subject, encoding = decode_header(msg["Subject"])[0]
                    if isinstance(subject, bytes):
                        subject = subject.decode(encoding if encoding else "utf-8")
                    from_ = msg.get("From")
                    date_ = msg.get("Date")
                    emails_content.append(
                        {"From": from_, "Subject": subject, "Date": date_}
                    )

        mail.logout()
        return emails_content

    except Exception as e:
        return [f"Fehler beim Abrufen des Gesendet-Ordners: {e}"]
