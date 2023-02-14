import imaplib

imap_server = "imap.rambler.ru"
imap_port = 993

result = []
with open("emails.txt", "r") as file:
    for line in file:
        email, password = line.strip().split(":")
        mail = imaplib.IMAP4_SSL(imap_server, imap_port)
        mail.login(email, password)
        mail.select("inbox")

        status, messages = mail.search(None, "ALL")
        if status == "OK":
            messages = messages[0].split(b" ")
            for message in messages[:50]:
                status, msg = mail.fetch(message, "(RFC822)")
                if status == "OK":
                    email_content = msg[0][1].decode("utf-8")
                    lines = email_content.splitlines()
                    subject = None
                    sender = None
                    for line in lines:
                        if line.startswith("Subject:"):
                            subject = line[9:]
                        if line.startswith("From:"):
                            sender = line[6:]
                    result.append((email, sender, subject))

        mail.close()
        mail.logout()


with open("email_result.txt", "w") as file:
    for email, sender, subject in result:
        file.write(f"{email} {sender} {subject}\n")
