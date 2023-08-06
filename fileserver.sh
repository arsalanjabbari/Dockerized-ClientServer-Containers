#!/bin/bash

# This script automates the process of building and running the server container for the Dockerized Client-Server Containers project.

# Create a Docker volume for server data storage
docker volume create servervol

# Create a user-defined network for the containers if it doesn't already exist
docker network create mynetwork 2> /dev/null || true

# Run the MongoDB container in the background
docker run --rm --network mynetwork --name mongo-container mongo:latest &

# Build the server container image
docker build -t server-image ./server

# Run the server container
docker run --rm -it \
  --network mynetwork \  # Connect to the specified network
  -p 8000:8000 \  # Map host port 8000 to container port 8000
  -v servervol:/serverdata \  # Mount the server volume to the container
  --name server-container \  # Assign a name to the container
  server-image  # Use the built server container image
