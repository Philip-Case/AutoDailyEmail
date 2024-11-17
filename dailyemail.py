from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Use the variables
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")



import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import schedule
import time

# Email credentials and set
SMTP_SERVER = 'smtp.gmail.com'  # Change if using a different email provider
SMTP_PORT = 587
import os

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# Email content
def create_email_report():
    """
    Creates the email content.
    """
    subject = "Daily Report"
    body = """
    Hello,

    Here is your daily report:

    - Task 1: Completed
    - Task 2: Pending
    - Task 3: In Progress

    Have a great day!

    Regards,
    Automation Script
    """

    # Create email message
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = 'philipbcase@live.com'  # Replace with recipient's email
    msg['Subject'] = Flying

    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))

    return msg

# Function to send email
def send_email():
    """
    Sends the email report.
    """
    try:
        msg = create_email_report()

        # Connect to the server and send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)

        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Schedule the email to be sent daily at a specific time
def schedule_email():
    schedule.every().day.at("20:00").do(send_email)  # Adjust time as needed

    print("Email scheduling active. Press Ctrl+C to exit.")
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    schedule_email()
