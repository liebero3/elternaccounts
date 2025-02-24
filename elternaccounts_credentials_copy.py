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

forms_message ="""Sehr geehrtes Elternteil,


wir haben Ihre Online-Registrierung für den Elternaccount erhalten und die Klassenlehrer darüber informiert.


Für die finale Aktivierung benötigen die Klassenlehrer noch den unterschriebenen Papierantrag. Falls Sie diesen noch nicht eingereicht haben, können Sie ihn unter [URL zum schriftlichen Antrag] herunterladen oder Ihr Kind kann ihn im Sekretariat abholen.


Bitte geben Sie den ausgefüllten Antrag beim Klassenlehrer Ihres Kindes ab. Nach Eingang des Antrags erhalten Sie innerhalb von 7 Tagen eine Bestätigungsmail mit einer Anleitung für den login. Sollte diese Mail ausbleiben, kontaktieren Sie bitte den Klassenlehrer per E-Mail, bei dem Sie den Antrag abgegeben haben.


Mit freundlichen Grüßen
ihr IT-Team vom Luisen-Gymnasium"""