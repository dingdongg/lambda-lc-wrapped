from datetime import date
import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content
from dotenv import load_dotenv
from email_template import load_email

envs = {}

# envs keys
API_KEY = "api_key"
FROM_EMAIL = "from_email"
TO_EMAIL = "to_email"

def load_envs():
    load_dotenv()
    envs[API_KEY] = os.environ.get("SENDGRID_API_KEY")
    envs[FROM_EMAIL] = os.environ.get("SENDGRID_SENDER_EMAIL")
    envs[TO_EMAIL] = os.environ.get("SENDGRID_RECIPIENT_EMAIL");

def send_email():
    sg = sendgrid.SendGridAPIClient(envs[API_KEY])

    from_email = Email(envs[FROM_EMAIL])
    to_email = To(envs[TO_EMAIL])
    subject = "🎁 WEEKLY LEETCODE WRAPPED"

    emailContent = load_email().render(bruh=date.today())
    content = Content("text/html", emailContent)

    mail = Mail(from_email, to_email, subject, content)
    mail_json = mail.get()

    try:
        res = sg.client.mail.send.post(request_body=mail_json)
        print("Email sent successfully.")
    except Exception as e:
        print(e)
        print("Something went wrong!")

if __name__ == "__main__": 
    load_envs()
    send_email()