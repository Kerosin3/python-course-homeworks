#!/usr/bin/zsh

docker build . -t web_app
docker run -p 5050:5000 web_app
