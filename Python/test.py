import requests
import smtplib
from email.mime.text import MIMEText

# Health check URL
health_url = "https://yourapp.example.com/health"

# Email config
smtp_server = "smtp.example.com"
smtp_port = 587
smtp_user = "sender@example.com"
smtp_pass = "your_password"
email_to = "recipient@example.com"

# Teams webhook URL
teams_webhook = "https://outlook.office.com/webhook/your_webhook_url"

try:
    response = requests.get(health_url, timeout=10)
    status = "UP" if response.status_code == 200 else f"DOWN (Status: {response.status_code})"
except Exception as e:
    status = f"ERROR: {e}"

# Send email
subject = f"App Health Status: {status}"
body = f"Health check for {health_url} returned: {status}"

msg = MIMEText(body)
msg["Subject"] = subject
msg["From"] = smtp_user
msg["To"] = email_to

try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_pass)
        server.sendmail(smtp_user, email_to, msg.as_string())
    print("Email sent.")
except Exception as e:
    print(f"Email error: {e}")

# Send to Teams
teams_message = {
    "text": f"**App Health Check**\nURL: {health_url}\nStatus: {status}"
}
try:
    teams_resp = requests.post(teams_webhook, json=teams_message)
    print("Teams notification sent." if teams_resp.status_code == 200 else f"Teams error: {teams_resp.text}")
except Exception as e:
    print(f"Teams error: {e}")
