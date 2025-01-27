import csv

def print_unique_emails():
    emails = set()
    with open('mails.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:  # Check for empty rows
                email = row[0].strip()  # Assuming email is in first column
                if email:
                    emails.add(email)
    # print(emails)
    for email in sorted(emails):
        print(email)

if __name__ == "__main__":
    print_unique_emails()
