#########################################################3
Get-Service # Retrieve the status of services
Get-Service -Name "Spooler" 
Get-Service -ComputerName server1 -Name "TeamCity Build Agent"

Start-Service -Name "TeamCity Build Agent" # Start a service 
Stop-Service -Name "wuauserv" # Stop a service 
Restart-Service -Name "Spooler" # Restart a service

Get-Process # View running processes 
Stop-Process -Name "notepad" # Terminate a process

Copy-Item -Path "C:\source\file.txt" -Destination "D:\backup\file.txt" # Copy files/folders

Move-Item -Path "C:\temp\log.txt" -Destination "C:\logs\log.txt" # Move files/folders

Remove-Item -Path "C:\temp\oldfile.txt" # Delete a file
Remove-Item -Path "C:\temp*" -Recurse -Force # Delete all files in a folder

Get-Content -Path "C:\logs\app.log" # Read a text file
Set-Content -Path "C:\output.txt" -Value "Hello, World!" # Write to a text file
Add-Content -Path "C:\output.txt" -Value "Another line" # Append to a text file

Test-Path -Path "C:\Windows\System32" # Check if a path exists

Invoke-Command -ComputerName server1 -ScriptBlock { Get-Service } # Run command on remote computer

Get-ChildItem -Path "C:\logs" # List files and directories

Set-ExecutionPolicy RemoteSigned # Change script execution policy

Get-EventLog -LogName Application -Newest 10 # Get latest event logs


#################################################################3
#Fetch agent details from TCE REst API and write to CSV
$teamcityUrl = "https://teamcity.example.com"
$teamcityUser = "your_username"
$teamcityToken = "your_token"  # Use a personal access token or password

# Prepare the REST API endpoint and headers
$uri = "$teamcityUrl/app/rest/agents"
$headers = @{
    Accept = "application/json"
}

# Create the credential for basic authentication
$pair = "$teamcityUser:$teamcityToken"
$bytes = [System.Text.Encoding]::UTF8.GetBytes($pair)
$base64 = [Convert]::ToBase64String($bytes)
$headers["Authorization"] = "Basic $base64"

# Output CSV file path
$outputCsv = "teamcity_agents.csv"

try {
    $response = Invoke-RestMethod -Uri $uri -Headers $headers -Method Get -TimeoutSec 10
    $agentList = @()
    if ($response.agent) {
        foreach ($agent in $response.agent) {
            $agentList += [PSCustomObject]@{
                ID        = $agent.id
                Name      = $agent.name
                Type      = $agent.type
                Connected = $agent.connected
            }
        }
        $agentList | Export-Csv -Path $outputCsv -NoTypeInformation -Encoding UTF8
        Write-Host "Agent list written to $outputCsv"
    } else {
        Write-Host "No agents found."
    }
}
catch {
    Write-Host "Error fetching agents: $($_.Exception.Message)"
}

###################################################################################

# mail from PS
# Email configuration
$smtpServer = "smtp.example.com"
$smtpPort = 587
$smtpUser = "sender@example.com"
$smtpPass = "your_password"
$from = "sender@example.com"
$to = "recipient@example.com"
$subject = "TeamCity Agents CSV"
$body = "Please find the attached TeamCity agents list."
$attachment = "C:\path\to\teamcity_agents.csv"

# Create a credential object
$securePass = ConvertTo-SecureString $smtpPass -AsPlainText -Force
$credential = New-Object System.Management.Automation.PSCredential($smtpUser, $securePass)

# Send the email with attachment
Send-MailMessage -From $from -To $to -Subject $subject -Body $body -SmtpServer $smtpServer `
    -Port $smtpPort -Credential $credential -UseSsl -Attachments $attachment


###########################################################################
#check service in remote server with credential
# List of remote servers
$servers = @("server1", "server2", "server3", "server4", "server5")
$serviceName = "TeamCity Build Agent"

# Prompt for credentials
$credential = Get-Credential

foreach ($server in $servers) {
    try {
        $status = Invoke-Command -ComputerName $server -Credential $credential -ScriptBlock {
            param($serviceName)
            $service = Get-Service -Name $serviceName -ErrorAction Stop
            return $service.Status
        } -ArgumentList $serviceName

        Write-Host "$server: $status"
    }
    catch {
        Write-Host "$server: ERROR - $($_.Exception.Message)"
    }
}

################################################################
#Copy config
# List of remote servers
$servers = @("server1", "server2", "server3")

# Path to the local config file and remote destination
$localConfig = "C:\local\path\myconfig.conf"
$remoteConfig = "C:\remote\path\myconfig.conf"

# Credentials (use with caution; for automation only)
$username = "DOMAIN\youruser"
$password = "yourpassword"  # Store securely in production!
$securePass = ConvertTo-SecureString $password -AsPlainText -Force
$credential = New-Object System.Management.Automation.PSCredential($username, $securePass)

foreach ($server in $servers) {
    try {
        # Copy the config file to the remote server
        Copy-Item -Path $localConfig -Destination $remoteConfig -ToSession `
            (New-PSSession -ComputerName $server -Credential $credential -Authentication Negotiate) -Force

        Write-Host "Config file replaced on $server"
    }
    catch {
        Write-Host "ERROR on $server: $($_.Exception.Message)"
    }
}

################################################################################
#download pkg from AF
# Artifactory and file details
$artifactoryUrl = "https://artifactory.example.com/artifacts/myapp.msi"  # or .exe
$destination = "C:\Temp\myapp.msi"  # or .exe
$apiKey = "your_artifactory_api_key"  # Use your actual API key

try {
    # Download the file from Artifactory
    Invoke-WebRequest -Uri $artifactoryUrl -OutFile $destination -Headers @{ "X-JFrog-Art-Api" = $apiKey }
    Write-Host "Downloaded file to $destination"

    # Install the MSI or EXE silently
    if ($destination -like "*.msi") {
        Start-Process msiexec.exe -ArgumentList "/i `"$destination`" /qn" -Wait
        Write-Host "MSI installation completed."
    } elseif ($destination -like "*.exe") {
        Start-Process $destination -ArgumentList "/S" -Wait  # /S is common for silent install; check your installer docs
        Write-Host "EXE installation completed."
    } else {
        Write-Host "Unknown file type: $destination"
    }
}
catch {
    Write-Host "ERROR: $($_.Exception.Message)"
}


######################################################################################
#get disk space
# Email configuration
$smtpServer = "smtp.example.com"
$smtpPort = 587
$smtpUser = "sender@example.com"
$smtpPass = "your_password"
$from = "sender@example.com"
$to = "recipient@example.com"
$subject = "Disk Space Report"

# Collect disk space info for all local drives
$results = Get-WmiObject Win32_LogicalDisk -Filter "DriveType=3" | 
    Select-Object DeviceID, 
                  @{Name="FreeGB";Expression={"{0:N2}" -f ($_.FreeSpace/1GB)}}, 
                  @{Name="TotalGB";Expression={"{0:N2}" -f ($_.Size/1GB)}}

# Convert results to HTML table for email body
$body = $results | ConvertTo-Html -Property DeviceID,FreeGB,TotalGB -Title "Disk Space Report" | Out-String

# Create a credential object for SMTP
$securePass = ConvertTo-SecureString $smtpPass -AsPlainText -Force
$credentialSmtp = New-Object System.Management.Automation.PSCredential($smtpUser, $securePass)

# Send the email
Send-MailMessage -From $from -To $to -Subject $subject -Body $body -BodyAsHtml `
    -SmtpServer $smtpServer -Port $smtpPort -Credential $credentialSmtp -UseSsl

Write-Host "Disk space report sent."

###########################################
#delete old files
# List of folders to clean
$folders = @(
    "C:\Temp\logs",
    "D:\AppData\oldfiles",
    "E:\Backups\archive"
)

foreach ($folder in $folders) {
    if (Test-Path $folder) {
        Get-ChildItem -Path $folder -File | Where-Object { $_.LastWriteTime -lt (Get-Date).AddDays(-30) } | Remove-Item -Force
        Write-Host "Cleaned files older than 30 days in $folder"
    } else {
        Write-Host "Folder not found: $folder"
    }
}
