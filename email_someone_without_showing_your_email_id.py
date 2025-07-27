
import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get email credentials securely
sender_email = os.getenv("EMAIL_ADDRESS")
app_password = os.getenv("APP_PASSWORD")

# Check if credentials were loaded correctly
if not sender_email or not app_password:
    print("❌ Email or password not found in environment variables.")
    exit()

# Compose the email
msg = EmailMessage()
msg['Subject'] = 'Anonymous Feedback'
msg['From'] = sender_email
msg['To'] = 'aniruddhgupta5@gmail.com'  # <-- change recipient as needed
msg.set_content("Hello! This mail is sent anonymously using Python 🐍.")

# Send the email
try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, app_password)
        smtp.send_message(msg)
    print("✅ Email sent successfully.")
except Exception as e:
    print(f"❌ Failed to send email: {e}")
