#!/bin/bash
poetry export -f requirements.txt --output requirements.txt
docker build -t juji-exercise .
