$git_log_output = git log --oneline --merges main -1
if ($git_log_output.Contains("into main")){
    write-host "merge to main detected, building and deploying"
    powershell.exe -NoProfile -ExecutionPolicy Bypass -File "C:\git\DiscordBots\LinkFixer\CICD\build.ps1"
}
