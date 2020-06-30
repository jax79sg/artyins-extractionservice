#!/bin/bash
docker rmi -f artyins-extractionservice
mkdir -p dockerdev
sudo rm -r dockerdev/artyins-extractionservice
rsync -r ../artyins-extractionservice dockerdev/
docker build ./dockerdev/. --no-cache -t artyins-extractionservice
