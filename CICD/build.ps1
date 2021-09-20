Set-Location -Path C:\git\DiscordBots\LinkFixer
$computerName = "COWSUNRAID"
$userId = "root"
$pass = Get-Content ".\_creds.txt" | ConvertTo-SecureString -AsPlainText -Force
$creds = New-Object System.Management.Automation.PSCredential -ArgumentList $userId, $pass
$packageName = "linkFixerImage_1_0_4.tar"



py -m pip freeze > $PWD\requirements.txt
docker build --tag link-fixer:1.0.4 .
docker save -o ..\$packageName link-fixer:1.0.4
Copy-Item -Path c:\git\DiscordBots\$packageName -Destination \\COWSUNRAID\Files\DiscordBots\LinkFixer



try {
    "Attempting SSH to $computerName"
    $sshSession = New-SSHSession -ComputerName $computerName -Credential $creds -AcceptKey -ConnectionTimeout 10 -ErrorAction Stop
    $sessionId = $sshSession.SessionId
    "Session $sessionId opened."
    $command = "docker load -i /mnt/user/Files/DiscordBots/LinkFixer/$packageName"
    "Command: {0}" -f $command
    $sshOut = (Invoke-SSHCommand -SessionId $sessionId -Command $command).Output
    "Results: '{0}'" -f $sshOut
    Remove-SSHSession -SessionId $sessionId | Out-Null
    "Session $sessionId closed."
}
catch {$_.exception.Message}
