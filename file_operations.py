"""
file_operations.py

This module provides functions to perform file operations with a Nextcloud server,
including downloading and uploading files using HTTP Basic Authentication.

Functions:
- get_file: Downloads a file from a specified URL.
- put_file: Uploads a local file to a specified URL.

This script requires the `requests` library and credentials defined in
the `elternaccounts_credentials` module.

Usage:
import file_operations

file_operations.get_file('https://example.com/path/to/file', 'local_file.txt', 'username', 'password') file_operations.put_file('https://example.com/upload/path', 'local_file.txt', 'username', 'password')

"""

import requests
from requests.auth import HTTPBasicAuth
import logging
import elternaccounts_credentials

# Logger für dieses Modul erstellen
logger = logging.getLogger(__name__)

NEXTCLOUD_USERNAME = elternaccounts_credentials.username
NEXTCLOUD_PASSWORD = elternaccounts_credentials.password


def get_file(url: str, filename: str, username: str, password: str) -> None:
    """
    Downloads a file from a specified URL and saves it locally.

    Parameters:
    - url (str): The URL from which the file will be downloaded.
    - filename (str): The local filename where the downloaded content will be saved.
    - username (str): The username for HTTP Basic Authentication.
    - password (str): The password for HTTP Basic Authentication.

    Logs:
    - Info: If the file is downloaded successfully.
    - Error: If the request fails with a status code other than 200.
    """
    response = requests.get(url, auth=HTTPBasicAuth(username, password))

    if response.status_code == 200:
        file_content = response.content
        with open(filename, "wb") as file:
            file.write(file_content)
        logger.info(f"Datei wurde heruntergeladen von {url}")
    else:
        logger.error(f"Fehler beim Zugriff auf die Datei: {response.status_code}")


def put_file(url: str, filename: str, username: str, password: str) -> None:
    """
    Uploads a local file to a specified URL.

    Parameters:
    - url (str): The URL to which the file will be uploaded.
    - filename (str): The local filename of the file to be uploaded.
    - username (str): The username for HTTP Basic Authentication.
    - password (str): The password for HTTP Basic Authentication.

    Logs:
    - Info: If the file is uploaded successfully.
    - Error: If the request fails with a status code other than 200, 201, or 204.
    """
    with open(filename, "rb") as file:
        file_content = file.read()
    response = requests.put(
        url, data=file_content, auth=HTTPBasicAuth(username, password)
    )

    if response.status_code in [200, 201, 204]:
        logger.info(f"Datei wurde hochgeladen zu {url}")
    else:
        logger.error(f"Fehler beim Hochladen der Datei: {response.status_code}")
