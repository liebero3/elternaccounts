"""
forms2.py

This module provides a class to interact with the Nextcloud Forms API, allowing
users to retrieve forms and their submissions. It supports authentication and 
uses RESTful endpoints provided by Nextcloud. The functionality includes getting 
all forms, shared forms, form submissions, and exporting form submissions in CSV format.

Usage:
    To use this module, instantiate the `NextcloudFormsAPI` class with valid 
    Nextcloud credentials, and call its methods to interact with the forms API.

Example:
    api = NextcloudFormsAPI(NEXTCLOUD_URL, NEXTCLOUD_USERNAME, NEXTCLOUD_PASSWORD)
    response = api.get_forms()
    print(response.text)

Dependencies:
    - requests: To make HTTP requests to the API.
    - elternaccounts_credentials: To securely handle and retrieve user credentials.
    - logging: For logging purposes in the module.
"""
import requests
import elternaccounts_credentials
import logging

logger = logging.getLogger(__name__)

NEXTCLOUD_USERNAME = elternaccounts_credentials.username
NEXTCLOUD_PASSWORD = elternaccounts_credentials.password
NEXTCLOUD_URL = elternaccounts_credentials.server_url


class NextcloudFormsAPI:
    """
    A class to interact with the Nextcloud Forms API.
    This class provides methods to interact with forms and their submissions 
    in a Nextcloud instance via the RESTful API provided by Nextcloud.

    Attributes:
        base_url (str): Base URL of the Nextcloud server's forms API.
        username (str): Username for authentication.
        password (str): Password for authentication.
        auth (tuple): Authentication tuple for requests library.
    """
    def __init__(self, base_url, username, password):
        """
        Initializes a new instance of the NextcloudFormsAPI class.

        Parameters:
            base_url (str): The base URL of the Nextcloud Forms API.
            username (str): The username for authenticating API requests.
            password (str): The password for authenticating API requests.
        """
        self.base_url = base_url
        self.username = username
        self.password = password
        self.auth = (username, password)

    def _request(self, method, endpoint, **kwargs):
        """
        Internal method to send HTTP requests to the Nextcloud Forms API.

        Parameters:
            method (str): HTTP method (e.g., "GET", "POST").
            endpoint (str): API endpoint to be appended to the base URL.
            **kwargs: Additional keyword arguments to pass to the requests.request() function.
        
        Returns:
            response (requests.Response): The HTTP response from the API call.

        Raises:
            HTTPError: If the HTTP request returned an unsuccessful status code.
        """
        url = f"{self.base_url}/ocs/v2.php/apps/forms/api/v2.4/{endpoint}"
        headers = {"OCS-APIRequest": "true", "Accept": "application/json"}
        response = requests.request(
            method, url, auth=self.auth, headers=headers, **kwargs
        )
        response.raise_for_status()
        return response

    def get_forms(self):
        """
        Retrieves all forms accessible to the user.

        Returns:
            response (requests.Response): The HTTP response containing the array of forms in JSON format.
        """
        return self._request("GET", "forms")

    def get_shared_forms(self):
        """
        Retrieves all forms shared with other users.

        Returns:
            response (requests.Response): The HTTP response containing shared forms in JSON format.
        """
        return self._request("GET", "shared_forms")

    def getFormSubmissions(self, formshash: str):
        """
        Retrieves submissions for a specific form.

        Parameters:
            formshash (str): The unique identifier for the form.
        
        Returns:
            response (requests.Response): The HTTP response containing submissions in JSON format.
        """
        return self._request("GET", f"submissions/{formshash}")

    def getFormSubmissionsCSV(self, formshash: str):
        """
        Retrieves submissions for a specific form in CSV format.

        Parameters:
            formshash (str): The unique identifier for the form.

        Returns:
            response (requests.Response): The HTTP response containing submissions in CSV format.
        """
        return self._request("GET", f"submissions/export/{formshash}")


if __name__ == "__main__":
    # Instantiate the API client with Nextcloud credentials
    api = NextcloudFormsAPI(NEXTCLOUD_URL, NEXTCLOUD_USERNAME, NEXTCLOUD_PASSWORD)
    # Example API call to get all forms
    r = api.get_forms()
    print(r.text)
    
