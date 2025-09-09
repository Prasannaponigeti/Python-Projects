import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import socket
socket.getaddrinfo('localhost', 8080)

#sender details
SENDER_EMAIL = "please select your email"
SENDER_PASSWORD ="enter passcode"
#configurations
SMTP_SERVER ='smtp.gmail.com'
SMTP_PORT = 587

#single sender function
def single_sender(to_email: str, subject: str, body:str = None):
    msg = MIMEMultipart()
    msg['To'] = to_email
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg.attach(MIMEText(body, 'plain'))

    #create server connection
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  #server starts securely
        #server login
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, to_email, msg.as_string())
        server.quit()  #close server
        print(f"email send successfully to {to_email}")
    except Exception as e:

        print(f"Failed to send email to {to_email}. Error: {e}")
