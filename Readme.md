# Build image
## Run locally docker
```bash
# Build docker image
docker build -t yt-dl-back .

# Run docker image
docker run -p 5000:5000 yt-dl-back
```

## Publish image
```bash
# Build image in repository
docker build -t <DOCKER_USER>/yt-dl-back .

# Push image in repository
docker push <DOCKER_USER>/yt-dl-back
```
