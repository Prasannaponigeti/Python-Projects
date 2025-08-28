import send_single_email
import send_bulk_emails



#main start
if __name__ == "__main__":
   print("Select type emails send\n 1. Single email send \n 2. Bulk email send")
   choice=int(input("Please select your type of email to send: "))
   subject = input("Enter subject of an email: ")
   body = input(" Enter body of an email: ")
   if choice==1:
    receiver_email = input("Enter receiver email: ")
      #send single main function call
    send_single_email.single_sender(
        to_email = receiver_email,
        subject = subject,
        body = body
    )
   elif choice==2:
     receiver_email_list=list(input("Enter all emails separated by comma: ").split(","))
     #send bulk emails function call
     send_bulk_emails.send_bulk_emails(
       emails=receiver_email_list,
       subject = subject,
       body=body,
     )
   
