import smtplib  # SMTP protocol se email bhejne ke liye
from email.message import EmailMessage  # Email object banane ke liye

from pathlib import Path  # HTML file ko read karne ke liye
from string import Template  # HTML me variables ($name) replace karne ke liye

# HTML file read karke Template object banao
html = Template(
    Path("index.html").read_text(encoding="utf-8")
)

# Email object banao
email = EmailMessage()

# Sender Name
email["From"] = "Ishika Gaur"

# Receiver Email
email["To"] = "t31610683@gmail.com"

# Email Subject
email["Subject"] = "Python HTML Email"

# HTML template me $name ki jagah "Ishika" daalo
email.set_content(
    html.substitute(name="Ishika"),
    subtype="html"   # Email ko HTML format me bhejo
)

# Gmail SMTP Server se connect karo
with smtplib.SMTP("smtp.gmail.com", 587) as smtp:

    smtp.ehlo()  # SMTP server ko Hello bolo

    smtp.starttls()  # Secure connection start karo

    # Gmail login (App Password use karo)
    smtp.login(
        "ishikalalitgaur521@gmail.com",
        "vcnc cczv peeg ickv"
    )

    # Email send karo
    smtp.send_message(email)

print("✅ HTML Email sent successfully!")