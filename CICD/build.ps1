py -m pip freeze > requirements.txt
docker build --tag link-fixer:v1.0.1 .
pscp -pw  c:\git\DiscordBots\dockerimage.tar pi@raspberrypi:"/home/pi/DiscordBots/LinkFixer"