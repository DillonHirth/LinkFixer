# Link Fixer Discord Bot

## The Why

- Dive into python and programming again to refresh and build on my college education.
- Get more experience with discord bots as I have a couple ideas regarding them.
- Have a fun project I can slowly expand on as I gain more knowledge of pytest, python structure, Linting...

## The What

This is a simple discord bot that fixes terrible ifunny.com mobile links that force a redirect to their website in order to view a video. So, in order to avoid this issue, I decided to automate the process.

## The How <sub>(to install)</sub>

### Locally
Once the repo is cloned, in the terminal run the below snippet to get up and running. make sure your terminal's working directory is the project root. 
```:
pip3.9 install pipenv
pipenv lock
pipenv install --dev
```
add a .env file into the root
```:
# .env
DISCORD_TOKEN=<copy your discord token here>
```
### Creating a Docker image

So, there are a lot of options out there for hosting a simple discord bot. Because this Bot should have fairly low overhead and the fact that I'm always looking for more uses for my server, I chose to host it on my Unraid server using Docker.
```python:
$packageName = "linkFixerImage.tar"
$imageName = "link-fixer:0.0.0"
docker build --tag $imageName .
docker save -o ..\$packageName $imageName #creates the tar, that can then be pushed where needed and loaded into docker
```

## Notes

### Dockerfile 

So the progression of the docker file was interesting. I started with the most basic dockerfile possible from the guide on dockers website
until I found this article: https://pythonspeed.com/articles/pipenv-docker/ and took what I found there to alter what I had. But, I wanted more.
running lock in docker to output a requirements file, didn't strike me as deterministic. Not to mention, I also really wanted to use pipenv for the entire process, not just half of it. So the rabbit hole got deeper.
My first change was to remove the 'pipenv lock', and change the process from 'install pipenv -> lock -> install' too 'install pipenv -> pipenv install' this kept the lock local pre-docker so the pipfile 
lock I copied over was the one it would use, instead of the requirements.txt it generated. It wasn't until I found this article: https://sourcery.ai/blog/python-docker/ that i figured out why that simple change wasn't working.
(the docker build would be successful, but the dependencies were not getting copied). The reason my change was failing (as I hopefully understand correctly) was due to the fact that I wasn't copying the dependencies that were installed to the venv.
Once I understood that, there were two ways around the issue. The more elegant/complicated solution described by the article above, and the simpler version I found on stack overflow('pipenv install --system --deploy --clear', the --system flag installs the venv in the project root where it gets copied over. https://stackoverflow.com/questions/58300046/how-to-make-lightweight-docker-image-for-python-app-with-pipenv).
In the end i chose the sourcery version, as the article was really well written, allowing me to be a bit more comfortable in my understanding of the code, plus the resulting image was ~80mb smaller.

A great link describing the difference/use of ENTRYPOINT vs CMD: https://stackoverflow.com/questions/21553353/what-is-the-difference-between-cmd-and-entrypoint-in-a-dockerfile