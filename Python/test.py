########################
# Python Automation Scripts
# Use: Admin, DevOps, Automation
########################

# -----------------------------
# 1. Check Status of Service (Local & Remote)
# -----------------------------
# For Windows systems
import subprocess

def check_service_status(service_name, remote_host=None):
    if remote_host:
        cmd = f"sc \\\\{remote_host} query {service_name}"
    else:
        cmd = f"sc query {service_name}"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(result.stdout)

# Usage:
# check_service_status("wuauserv")  # Local
# check_service_status("wuauserv", "RemotePC")  # Remote


# -----------------------------
# 2. Replace Config File
# -----------------------------
import shutil

def replace_config(src, dst):
    shutil.copyfile(src, dst)
    print(f"Config replaced: {dst}")

# Usage:
# replace_config("new_config.ini", "/etc/app/config.ini")


# -----------------------------
# 3. Get Disk Space (Remote via Paramiko) & Email CSV
# -----------------------------
import paramiko
import csv
import smtplib
from email.message import EmailMessage

def get_disk_space_remote(host, user, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=user, password=password)
    stdin, stdout, stderr = ssh.exec_command("df -h /")
    output = stdout.read().decode()
    ssh.close()
    return output

# Write to CSV and send via email
def send_disk_report_csv(hosts):
    with open("disk_report.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Host", "DiskInfo"])
        for host in hosts:
            info = get_disk_space_remote(host, "username", "password")
            writer.writerow([host, info])
    
    msg = EmailMessage()
    msg["Subject"] = "Disk Space Report"
    msg["From"] = "admin@domain.com"
    msg["To"] = "ops@domain.com"
    msg.set_content("Attached is the disk space report.")
    with open("disk_report.csv", "rb") as f:
        msg.add_attachment(f.read(), maintype='text', subtype='csv', filename="disk_report.csv")
    
    with smtplib.SMTP("smtp.domain.com") as s:
        s.send_message(msg)

# Usage:
# send_disk_report_csv(["10.0.0.1", "10.0.0.2"])


# -----------------------------
# 4. Get Folder Size Recursively
# -----------------------------
import os

def get_folder_sizes(path):
    for root, dirs, files in os.walk(path):
        size = sum(os.path.getsize(os.path.join(root, f)) for f in files)
        print(f"{root}: {round(size / (1024*1024), 2)} MB")

# Usage:
# get_folder_sizes("/var/log")


# -----------------------------
# 5. Download from Artifactory & Install MSI (Windows)
# -----------------------------
import requests
import subprocess

def download_artifact(url, username, password, out_file):
    r = requests.get(url, auth=(username, password))
    with open(out_file, "wb") as f:
        f.write(r.content)

def install_msi(file_path):
    subprocess.run(["msiexec", "/i", file_path, "/quiet", "/norestart"], shell=True)

# Usage:
# download_artifact("https://repo/artifact.msi", "user", "pass", "file.msi")
# install_msi("file.msi")


# -----------------------------
# 6. Exception Handling
# -----------------------------
try:
    risky = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
finally:
    print("Cleanup actions here.")


# -----------------------------
# 7. REST API: Fetch User Data, Save to YAML
# -----------------------------
import requests
import yaml

def fetch_users_to_yaml(api_url, out_file):
    resp = requests.get(api_url)
    data = resp.json()
    with open(out_file, "w") as f:
        yaml.dump(data, f)

# Usage:
# fetch_users_to_yaml("https://api.example.com/users", "users.yaml")


# -----------------------------
# 8. REST API: POST, PUT, DELETE
# -----------------------------
# Using requests library
def rest_api_example():
    url = "https://api.example.com/resource"
    headers = {"Content-Type": "application/json"}

    # POST
    post_data = {"name": "test"}
    post_resp = requests.post(url, json=post_data, headers=headers)

    # PUT
    put_data = {"name": "updated"}
    put_resp = requests.put(url + "/1", json=put_data, headers=headers)

    # DELETE
    del_resp = requests.delete(url + "/1", headers=headers)

    print("POST:", post_resp.status_code)
    print("PUT:", put_resp.status_code)
    print("DELETE:", del_resp.status_code)

# Usage:
# rest_api_example()


# -----------------------------
# 9. Get Variable from Vault (HashiCorp Vault Example)
# -----------------------------
import hvac

def get_vault_secret(vault_addr, token, secret_path):
    client = hvac.Client(url=vault_addr, token=token)
    secret = client.secrets.kv.v2.read_secret_version(path=secret_path)
    return secret['data']['data']

# Usage:
# secret = get_vault_secret("http://localhost:8200", "s.XXXXXX", "secret/api-key")
# print(secret)


# -----------------------------
# 10. Use Proxy with Requests
# -----------------------------
proxies = {
    "http": "http://proxy.company.com:8080",
    "https": "http://proxy.company.com:8080",
}

resp = requests.get("https://api.example.com/data", proxies=proxies)
print(resp.json())




#####################################################
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
