# Placeholder for credentials and configuration. 
# Populate these with actual values as needed.

# Credentials for the Nextcloud user
username = "your_nextcloud_username"
password = "your_nextcloud_password"

# Server URLs
server_url = 'https://yourserver.example.com'
url = f'{server_url}/ocs/v2.php/'
url1 = f'{server_url}/ocs/v1.php/'
url2 = f'{server_url}/index.php/'
url3 = f'{server_url}/ocs/v1.php/cloud'
form = '/your_form_id'
elternaccounts = "your_elternaccounts_id"
url_elternaccounts_backup = f'{server_url}/remote.php/dav/files/your_username/your_path/elternzugaenge_webuntis.xlsx'
url_export = f'{server_url}/remote.php/dav/files/your_username/your_path/'
url_elterncsv = f'{server_url}/remote.php/dav/files/your_username/your_path/elternaccounts.csv'
url_elterncsvcontrol = f'{server_url}/remote.php/dav/files/your_username/your_path/elternaccounts-control.csv'
url_elternaccounts_share = f'{server_url}/remote.php/dav/files/your_username/your_share_path/elternzugaenge_webuntis.xlsx'

# Mail credentials
smtp_server = 'your_smtp_server'
smtp_port = 465  # Ensure this is the correct port
imap_server = 'your_imap_server'
imap_port = 993  # Ensure this is the correct port
mail_benutzername = 'your_email@example.com'
mail_passwort = 'your_email_password'

# Mail-Body
mailtext = """Guten Tag,

die Webuntis-Elternaccounts wurden erstellt. Bitte folgen Sie UNBEDINGT der Anleitung hier: 

https://url_zur_anleitung/

Sollten Sie bereits einen funktionierenden Account haben ignorieren Sie die Mail bitte.

Freundliche Grüße
Your Name
"""
