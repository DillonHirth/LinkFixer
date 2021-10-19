# Link Fixer Discord Bot

## The Why

- Dive into python and programming again to refresh and build on my college education.
- Get more experience with discord bots as I have a couple ideas regarding them.
- Have a fun project I can slowly expand on as I gain more knowledge of pytest, python structure, Linting...

## The What

This is a simple discord bot that fixes terrible ifunny.com mobile links that force a redirect to their website in order to view a video. So, in order to avoid this issue, I decided to automate the process.

## The How <sub>(to install)</sub>

So, there are alot of options out there for hosting a simple discord bot. Because this one should have fairly low overhead, I chose to host it on my Unraid server using Docker.


<pre><code>
$packageName = "linkFixerImage.tar"
$imageName = "link-fixer:0.0.0"
docker build --tag $imageName .
docker save -o ..\$packageName $imageName
</code></pre>
## The Future

- Tests, Tests, and more Tests please
- Better link detection
- More URL's
- Add Bot commands
- I need to comment my code
- Logging. Better output while running and building. 