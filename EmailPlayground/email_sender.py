import smtplib #built-in module for sending emails using the Simple Mail Transfer Protocol (SMTP)
from email.message import EmailMessage

# Email object banao
email = EmailMessage()

# Sender
email["from"] = "ishika"

# Receiver
email["to"] = "t31610683@gmail.com"

# Subject
email["subject"] = "You won $1,000,000"

# Email body
email.set_content("I am a Python master.")

# Gmail SMTP server se connect karo
with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:

    # SMTP protocol start  Extended Hello
    smtp.ehlo()

    # Secure connection banao  Transport Layer Security
    smtp.starttls()

    # Gmail login
    smtp.login("ishikalalitgaur521@gmail.com", "vcnc cczv peeg ickv")

    # Email send karo
    smtp.send_message(email)

print("✅ Email sent successfully!")