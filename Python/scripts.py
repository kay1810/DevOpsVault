import requests
import csv
uri= "https://reqres.in/api/users"
post_data={
    "name": "morpheus",
    "job": "leader"
}
bearer_token = "reqres-free-v1"  # Replace with your actual token

put_data={

     "name": "morpheus",
    "job": "team leader"
}
headers = {
    "x-api-key": "reqres-free-v1",
    "Content-Type": "application/json"
}

try:
    res= requests.post(uri,json=post_data,headers=headers)
    print(res.status_code)
    print(res.json())

    put_res=requests.put(f"{uri}/2",json=put_data,headers=headers)
    print(put_res.status_code)
    print(put_res.json())


    delete_response = requests.delete(f"{uri}/2", headers=headers)
    print("DELETE response:", delete_response.status_code)
    response=requests.get(uri)
    data = response.json()
    users=data["data"]
    #for user in data["data"]:
     #  print(user["email"])
    
    with open("new.csv","w", newline="" ) as f:
        fieldnames = ["id", "email", "first_name", "last_name", "avatar"]
        writer= csv.DictWriter(f,fieldnames=fieldnames)
        writer.writeheader()
        for user in users:
            writer.writerow(user)

except Exception as e:
    print(f"error occured:{e}")

#######################################

import requests
import csv
import smtplib
from email.message import EmailMessage

api_url = "https://reqres.in/api/users"
bearer_token = "YOUR_BEARER_TOKEN"  # Replace with your actual token

headers = {
    "Authorization": f"Bearer {bearer_token}"
}

response = requests.get(api_url, headers=headers)
data = response.json()
users = data["data"]

csv_filename = "users.csv"
with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["id", "email", "first_name", "last_name", "avatar"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for user in users:
        writer.writerow(user)

print("Exported users to users.csv")

# Email the CSV file
sender_email = "your_email@example.com"
receiver_email = "recipient@example.com"
subject = "User List CSV"
body = "Please find attached the users.csv file."

msg = EmailMessage()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = subject
msg.set_content(body)

# Attach the CSV file
with open(csv_filename, "rb") as f:
    msg.add_attachment(f.read(), maintype="text", subtype="csv", filename=csv_filename)

# Send the email (using SMTP server, e.g., Gmail SMTP)
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_user = "your_email@example.com"
smtp_password = "your_email_password"  # Use app password if using Gmail with 2FA

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_user, smtp_password)
    server.send_message(msg)

print("Email sent with users.csv attached.")

#####################################

input_log="test.log"
output="warnings.txt"

with open(input_log, "r", encoding="utf-8") as logfile,open(output,"w") as outfile:
    for line in logfile:
        if "warning" in line.lower():
            outfile.write(line)
#################################

import requests
import json

# URL to check
url = "https://example.com"  # Replace with your web URL

# Microsoft Teams webhook URL
teams_webhook = "https://outlook.office.com/webhook/..."  # Replace with your Teams webhook URL

# Check health
try:
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        status = f"✅ {url} is UP (status code: {response.status_code})"
    else:
        status = f"⚠️ {url} returned status code: {response.status_code}"
except Exception as e:
    status = f"❌ {url} is DOWN. Error: {str(e)}"

# Post to Teams
payload = {
    "text": status
}

headers = {
    "Content-Type": "application/json"
}

teams_response = requests.post(teams_webhook, data=json.dumps(payload), headers=headers)

if teams_response.status_code == 200:
    print("Posted health status to Teams.")
else:
    print(f"Failed to post to Teams: {teams_response.status_code} {teams_response.text}")

#################################################
import requests
import json
import logging
import config


#logger = logging.getLogger(__name__)
#logger.setLevel(logging.INFO)

headers = {"Content-Type":"application/json","Accept":"application/json"}

def createChange(payload):
    try:
        createChange_URL=f"{config.SERVICENOW_URL}/sn_chg_rest/change/normal"
        response = requests.post(createChange_URL,auth=(config.USERNAME,config.PASSWORD),headers=headers,data=json.dumps(payload))
        if response.status_code == 200: 
            print("Change Created Successfully")
            data = response.json()
            print(data)
            global Change_sys_id
            global Change_number
            Change_sys_id=data['result']['sys_id']['value']
            Change_number=data['result']['number']['value']
            print(f"Change {Change_number} Created Successfully")
            print(f"Change sys id - {Change_sys_id}")
        else:
            data = response.json()
            print(response.status_code, data)
            print (f"Failed to create Change:{response.status_code}- {response.text}")
    except requests.exceptions.RequestException as err:
        print(f"Error while creating Change: {err}")

def UpdateChangeInfo(sys_id,payload):
    try:
        EditChange_URL=  f"{config.SERVICENOW_URL}/sn_chg_rest/change/{sys_id}"
        response = requests.patch(EditChange_URL,auth=(config.USERNAME,config.PASSWORD),headers=headers,json=payload)
        if response.status_code == 200: 
            print("Change Updated Successfully")
            data = response.json()
            print(data)
        else:
            print (f"Failed to update Change:{response.status_code}- {response.text}")
    except requests.exceptions.RequestException as err:
        print(f"Error while updating Change: {err}")

def AddImpactedCI(change_sys_id,CMDB_CI_value):
    try:
        AddCI_URL=f"{config.SERVICENOW_URL}/sn_chg_rest/change/{change_sys_id}/ci"
        data = {
            "cmdb_ci_sys_ids":f"{CMDB_CI_value}",
            "association_type":"impacted"
        }
        response = requests.post(AddCI_URL,auth=(config.USERNAME,config.PASSWORD),headers=headers,json=data)
        if response.status_code == 202: 
            print("CI added Successfully")
            data = response.json()
            print(response.status_code, data)
        else:
            data = response.json()
            print(response.status_code, data)
            print (f"Failed to add Impacted CI to Change:{response.status_code}- {response.text}")
    except requests.exceptions.RequestException as err:
        print(f"Error while adding Impacted CI to Change: {err}")

def DeleteImpactedCI(CI_sys_id):
    try:
        
        #pass the sys_id of the impacted CI entry to delete
        DeleteCI_URL=f"{config.SERVICENOW_URL}/now/table/task_cmdb_ci_service/{CI_sys_id}"
        response = requests.delete(DeleteCI_URL,auth=(config.USERNAME,config.PASSWORD),headers=headers)
        print(response)
        if response.status_code == 204: 
            print("Impacted CI removed  Successfully")
                        
        else:
            data = response.json()
            print(response.status_code, data)
            print (f"Failed to remove Impacted CI:{response.status_code}- {response.text}")
    except requests.exceptions.RequestException as err:
        print(f"Error while removing Impacted CI: {err}")

def GetImpactedCIs(change_sys_id):
    try:
        
        GetCI_URL=f"{config.SERVICENOW_URL}/sn_chg_rest/change/{change_sys_id}/ci?association_type=impacted"
        response = requests.get(GetCI_URL,auth=(config.USERNAME,config.PASSWORD),headers=headers)
        data = response.json()
        #print(response.json())
        if response.status_code == 200: 
            print("Fetched Impacted CIs")
            
            ImpactedCIs=data['result']
            for ci in ImpactedCIs:
                print(f"{ci['cmdb_ci_service']} with sys_id : {ci['sys_id']['value']}")
                CI_name=ci['cmdb_ci_service']['display_value']
                CI_linked_value=ci['sys_id']['value']
                Current_ImpactedCI_list[CI_name]=CI_linked_value

                        
        else:
            data = response.json()
            print(response.status_code, data)
            print (f"Failed to Fetch Impacted CIs:{response.status_code}- {response.text}")
    except requests.exceptions.RequestException as err:
        print(f"Error while fetching Impacted CIs: {err}")

def UpdateImpactedCI(change_sys_id):
    cmdb_sys_ids_to_remove=[]
    cmdb_ids_to_add=[]

    #Check if any valid CI is not present in Impacted_CIs list
    for cmdb_name,value in config.VALID_IMPACTED_CI_LIST.items():
        if cmdb_name not in Current_ImpactedCI_list:
            cmdb_ids_to_add.append(value)

    #Check which extra CIs are present in Impacted_CIs list
    for cmdb_name,sys_id in Current_ImpactedCI_list.items():
        if cmdb_name not in config.VALID_IMPACTED_CI_LIST:
            cmdb_sys_ids_to_remove.append(sys_id)

    #print(f"CIs to add: {cmdb_ids_to_add}")
    #print(f"CIs to remove: {cmdb_sys_ids_to_remove} ")

    if len(cmdb_ids_to_add) !=0:
        for entry in cmdb_ids_to_add:
            AddImpactedCI(change_sys_id,entry)
            print(f"Added {entry}")
    else:
        print("No additional CIs to be added to impacted CIs list")

    if len(cmdb_sys_ids_to_remove) !=0:
        for entry in cmdb_sys_ids_to_remove:
            DeleteImpactedCI(entry)
            print(f"Deleted {entry}")
    else:
        print("No CIs to be removed from impacted CIs list")

    

def AddAttachment(change_sys_id):
    try:
        filenamepath="U:/SRE project/ServiceNowAPI/test2.txt"
        
        Addfile_URL=f"{config.SERVICENOW_URL}/now/attachment/file?table_name=change_request&table_sys_id={change_sys_id}&file_name=test2.txt"
        
        with open(filenamepath, 'rb') as f:
            file_data= f.read()

        files = {
            'file':('file.txt',file_data,'application/octet-stream')
        }
        
        response = requests.post(Addfile_URL,auth=(config.USERNAME,config.PASSWORD),headers=headers,files=files)
        if response.status_code == 201: 
            print("File Added Successfully")
            data = response.json()
            print(response.status_code, data)
        else:
            data = response.json()
            print(response.status_code, data)
            print (f"Failed to add file:{response.status_code}- {response.text}")
    except requests.exceptions.RequestException as err:
        print(f"Error while adding file: {err}")


def fetch_change_tasks(change_sys_id):
    try:
        FetchTask_URL=f"{config.SERVICENOW_URL}/sn_chg_rest/change/{change_sys_id}/task?sysparm_query=active=true"
        response = requests.get(FetchTask_URL,auth=(config.USERNAME,config.PASSWORD),headers=headers)
        #print(response)
        if response.status_code == 200: 
            print("Tasks fetched successfully")
            data = response.json()
            tasks=data['result']
            for task in tasks:
                tasknumber=task['number']
                assgn_group=task['assignment_group']
                task_ci=task['cmdb_ci']
                print(f"Tasknumber:{tasknumber},Assignmentgroup:{assgn_group},Task_CI:{task_ci}")
                        
        else:
            data = response.json()
            print(response.status_code, data)
            print (f"Failed to Fetch Tasks:{response.status_code}- {response.text}")
    except requests.exceptions.RequestException as err:
        print(f"Error while fetching Tasks: {err}")    


def Update_Change_tasks(change_sys_id):
    try:
        FetchTask_URL=f"{config.SERVICENOW_URL}/sn_chg_rest/change/{change_sys_id}/task?sysparm_query=active=true"
        response = requests.get(FetchTask_URL,auth=(config.USERNAME,config.PASSWORD),headers=headers)
        #print(response)
        if response.status_code == 200: 
            print("Tasks fetched successfully")
            data = response.json()
            tasks=data['result']
            for task in tasks:
                tasknumber=task['number']['value']
                task_sys_id=task['sys_id']['value']
                assgn_group=task['assignment_group']
                task_ci=task['cmdb_ci']
                print(f"Tasknumber:{tasknumber},Assignmentgroup:{assgn_group},Task_CI:{task_ci}")
                
                if(task['change_task_type']['value']=='implementation'):
                    UpdateTask_URL=f"{config.SERVICENOW_URL}/sn_chg_rest/change/{change_sys_id}/task/{task_sys_id}"
                    task_payload={
                        "assignment_group": "t",
                        "cmdb_ci": 'ServiceNow - CMDB'
                    }
                    response = requests.patch(UpdateTask_URL,auth=(config.USERNAME,config.PASSWORD),headers=headers,json=task_payload)
                    print(response)
                    if response.status_code == 200: 
                        print("Task Updated Successfully")
                        #data = response.json()
                        #print(data)
                    else:
                        print (f"Failed to update Task:{response.status_code}- {response.text}")
                                        
        else:
            data = response.json()
            print(response.status_code, data)
            print (f"Failed to Fetch Tasks:{response.status_code}- {response.text}")
    except requests.exceptions.RequestException as err:
        print(f"Error while fetching Tasks: {err}")  

def Create_Change_task(change_sys_id):
    try:
        CreateTask_URL=f"{config.SERVICENOW_URL}/sn_chg_rest/change/{change_sys_id}/task"
        task_payload={
                        "assignment_group": "test",
                        "short_description": 'Suppress Alerts during Change Window'
        }
        response = requests.post(CreateTask_URL,auth=(config.USERNAME,config.PASSWORD),headers=headers,json=task_payload)
        print(response)
        if response.status_code == 200: 
            print("Task created successfully")
            
                                        
        else:
            data = response.json()
            print(response.status_code, data)
            print (f"Failed to crate Task:{response.status_code}- {response.text}")
    except requests.exceptions.RequestException as err:
        print(f"Error while creating new Task: {err}")
