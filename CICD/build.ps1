Set-Location -Path C:\git\DiscordBots\LinkFixer
$computerName = "COWSUNRAID"
$userId = "root"
$pass = Get-Content ".\.creds" | ConvertTo-SecureString -AsPlainText -Force
$creds = New-Object System.Management.Automation.PSCredential -ArgumentList $userId, $pass
$major = 1
$minor = 0
$patch = 7
$version = "$major.$minor.$patch"
$packageName = "linkFixerImage_$version.tar"
$imageName = "link-fixer:$version"
$containerName = "linkfixer"

docker build --tag $imageName .
docker save -o ..\$packageName $imageName
Copy-Item -Path c:\git\DiscordBots\$packageName -Destination \\COWSUNRAID\Files\DiscordBots\LinkFixer

try {
#open SSH session
    "Attempting SSH to $computerName"
    $sshSession = New-SSHSession -ComputerName $computerName -Credential $creds -AcceptKey -ConnectionTimeout 10 -ErrorAction Stop
    $sessionId = $sshSession.SessionId
    "Session $sessionId opened."


#delete the previous docker image and load the new docker image
    $command = "docker rmi $(docker images "link-fixer" -q)"
    "Command: {0}" -f $command
    $sshOut = (Invoke-SSHCommand -SessionId $sessionId -Command $command).Output
    "Results: '{0}'" -f $sshOut

    $command = "docker load -i /mnt/user/Files/DiscordBots/LinkFixer/$packageName"
    "Command: {0}" -f $command
    $sshOut = (Invoke-SSHCommand -SessionId $sessionId -Command $command).Output
    "Results: '{0}'" -f $sshOut


#stop and delete the old container
    $command = "docker stop $containerName"
    "Command: {0}" -f $command
    $sshOut = (Invoke-SSHCommand -SessionId $sessionId -Command $command).Output
    "Results: '{0}'" -f $sshOut

    $command = "docker rm $containerName"
    "Command: {0}" -f $command
    $sshOut = (Invoke-SSHCommand -SessionId $sessionId -Command $command).Output
    "Results: '{0}'" -f $sshOut


#create and start the new container
    $command = "docker create --name $containerName $imageName"
    "Command: {0}" -f $command
    $sshOut = (Invoke-SSHCommand -SessionId $sessionId -Command $command).Output
    "Results: '{0}'" -f $sshOut

    $command = "docker start $containerName"
    "Command: {0}" -f $command
    $sshOut = (Invoke-SSHCommand -SessionId $sessionId -Command $command).Output
    "Results: '{0}'" -f $sshOut


#close the session
    Remove-SSHSession -SessionId $sessionId | Out-Null
    "Session $sessionId closed."
}
catch {$_.exception.Message}