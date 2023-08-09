import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.template.loader import render_to_string
from os import getenv




def send_email(name, message, recipient):
   sender = getenv("EMAIL_ID")
   password = getenv("EMAIL_PASS")

   msg_for_me = MIMEText(message)
   msg_for_me['Subject'] = f'{name} - Contact from Portfolio'
   msg_for_me['From'] = sender
   msg_for_me['To'] = sender

   # Render the HTML email template with dynamic data
   html_message = render_to_string('email.html', {'name': name})
   
   # Set up the MIME object
   msg_for_client = MIMEMultipart('alternative')
   msg_for_client['Subject'] = 'Thank You for Reaching Out'
   msg_for_client['From'] = sender
   msg_for_client['To'] = recipient

   # Attach the HTML content
   msg_for_client.attach(MIMEText(html_message, 'html'))
   
   with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
      smtp_server.login(sender, password)
      smtp_server.sendmail(msg_for_me['From'], msg_for_me['To'], msg_for_me.as_string())
      smtp_server.sendmail(msg_for_client['From'], msg_for_client['To'], msg_for_client.as_string())

