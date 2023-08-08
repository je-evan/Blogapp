import smtplib
from email.mime.text import MIMEText
from os import getenv


def send_email(name, message, recipient):
    sender = getenv("EMAIL_ID")
    password = getenv("EMAIL_PASS")
    msg = MIMEText(message)
    msg['Subject'] = f'Contact from Portfolio - {name}'
    msg['From'] = sender
    msg['To'] = recipient
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipient, msg.as_string())
    print("Message sent!")

