Set-Location -Path C:\git\DiscordBots\LinkFixer
$computerName = "COWSUNRAID"
$userId = "root"
$pwd = Get-Content "$PSScriptRoot\_creds.txt" | ConvertTo-SecureString
$creds = New-Object System.Management.Automation.PSCredential -ArgumentList $userId, $pwd



py -m pip freeze > requirements.txt
docker build --tag link-fixer:v1.0.4 .
docker save -o .\linkFixerImage_v1_0_4.tar link-fixer:v1.0.4
Copy-Item -Path c:\git\DiscordBots\linkFixerImage_v1_0_1.tar -Destination \\COWSUNRAID\Files\DiscordBots\LinkFixer



try {
    "Attempting SSH to $computerName"
    $sshSession = New-SSHSession -ComputerName $computerName -Credential $creds -AcceptKey -ConnectionTimeout 10 -ErrorAction Stop
    $sessionId = $sshSession.SessionId
    "Session $sessionId opened."
    $command = "docker load -i /mnt/user/Files/linkFixerImage_v1_0_4.tar"
    "Command: {0}" -f $command
    $sshOut = (Invoke-SSHCommand -SessionId $sessionId -Command $command).Output
    "Results: '{0}'" -f $sshOut
    Remove-SSHSession -SessionId $sessionId | Out-Null
    "Session $sessionId closed."
}
catch {$_.exception.Message}
