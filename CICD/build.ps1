Set-Location -Path C:\git\DiscordBots\LinkFixer
$computerName = "COWSUNRAID"
$userId = "root"
$pass = Get-Content ".\_creds.txt" | ConvertTo-SecureString -AsPlainText -Force
$creds = New-Object System.Management.Automation.PSCredential -ArgumentList $userId, $pass
$packageName = "linkFixerImage_1_0_5.tar"
$imageName = "link-fixer:1.0.5"
$containerName = "linkfixer"



py -m pip freeze > $PWD\requirements.txt
docker build --tag $imageName .
docker save -o ..\$packageName $imageName
Copy-Item -Path c:\git\DiscordBots\$packageName -Destination \\COWSUNRAID\Files\DiscordBots\LinkFixer


#open SSH session
try {
    "Attempting SSH to $computerName"
    $sshSession = New-SSHSession -ComputerName $computerName -Credential $creds -AcceptKey -ConnectionTimeout 10 -ErrorAction Stop
    $sessionId = $sshSession.SessionId
    "Session $sessionId opened."
}
catch {$_.exception.Message}

#delete the previous docker image and load the new docker image
try {
    $command = " docker rmi $(docker images "link-fixer" -q)"
    "Command: {0}" -f $command
    $sshOut = (Invoke-SSHCommand -SessionId $sessionId -Command $command).Output
    "Results: '{0}'" -f $sshOut

    $command = "docker load -i /mnt/user/Files/DiscordBots/LinkFixer/$packageName"
    "Command: {0}" -f $command
    $sshOut = (Invoke-SSHCommand -SessionId $sessionId -Command $command).Output
    "Results: '{0}'" -f $sshOut
}
catch {$_.exception.Message}

#stop and delete the old container
try {
    $command = "docker stop $containerName"
    "Command: {0}" -f $command
    $sshOut = (Invoke-SSHCommand -SessionId $sessionId -Command $command).Output
    "Results: '{0}'" -f $sshOut

    $command = "docker rm $containerName"
    "Command: {0}" -f $command
    $sshOut = (Invoke-SSHCommand -SessionId $sessionId -Command $command).Output
    "Results: '{0}'" -f $sshOut
}
catch {$_.exception.Message}

#create and start the new container
try {
    $command = "docker create --name $containerName $imageName"
    "Command: {0}" -f $command
    $sshOut = (Invoke-SSHCommand -SessionId $sessionId -Command $command).Output
    "Results: '{0}'" -f $sshOut

    $command = "docker start $containerName"
    "Command: {0}" -f $command
    $sshOut = (Invoke-SSHCommand -SessionId $sessionId -Command $command).Output
    "Results: '{0}'" -f $sshOut
}
catch {$_.exception.Message}

#close the session
try {
    Remove-SSHSession -SessionId $sessionId | Out-Null
    "Session $sessionId closed."
}
catch {$_.exception.Message}