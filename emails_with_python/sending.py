import smtplib
import getpass
with smtplib.SMTP('smtp.gmail.com', 587) as smtp_object:
    smtp_object.ehlo()
    smtp_object.starttls()
    email = getpass.getpass("Email: ")
    password = getpass.getpass("Password ")
    smtp_object.login(email, password)
    from_address = email
    to_address = input("Enter email address")
    subject = input("Enter subject line")
    message = input("Enter a message")
    msg = "Subject: " + subject + '\n' + message
    smtp_object.sendmail(from_address, to_address, msg)
    smtp_object.quit()
