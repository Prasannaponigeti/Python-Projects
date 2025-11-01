import send_single_email

#create bulk email send email
def send_bulk_emails(emails:list, subject:str, body:str):
    for to_email in emails:
        try:
            send_single_email.single_sender(
                 to_email=to_email.strip(),
                 subject=subject,
                 body=body,
            )
            print(f"email send successfully to {to_email}")
        except Exception as e:
            print(f" Failed to send email to {to_email}. Error: {e}")