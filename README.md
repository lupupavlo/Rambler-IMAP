Description
This is a Python script that can be used to fetch the details of the first 50 emails from the "inbox" of multiple email accounts using IMAP protocol. The script reads the email accounts and passwords from a file named "emails.txt" and stores the email address, sender and subject of each email in a file named "email_result.txt". The script uses the imaplib module to connect to an email server and fetch the email details.

Instructions
To use this script, follow these steps:

Make sure you have Python 3 installed on your computer. If not, download and install it from the official Python website: https://www.python.org/downloads/
Clone the repository from GitHub to your local machine using the git clone command or by downloading the ZIP file and extracting it.
Open the emails.txt file and add the email accounts and passwords that you want to fetch details from, one per line in the format "email:password". Make sure the email accounts have IMAP access enabled.
Save the emails.txt file and run the script from the command line using the python command: python fetch_emails.py
Wait for the script to finish fetching the email details. The progress will be printed to the command line.
Once the script finishes running, open the email_result.txt file to see the email details that were fetched.
Note: This script is intended for educational and research purposes only. Use it responsibly and respect the privacy of others.
