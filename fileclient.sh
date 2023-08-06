#!/bin/bash

# This script automates the process of building and running the client container for the Dockerized Client-Server Containers project.

# Create a Docker volume for client data storage
docker volume create clientvol

# Build the client container image
docker build -t client-image ./client

# Run the client container
docker run --rm -it \
  --network mynetwork \  # Connect to the specified network
  -v clientvol:/clientdata \  # Mount the client volume to the container
  -e SERVER_HOST=server-container \  # Set the server's hostname
  -e SERVER_PORT=8000 \  # Set the server's port
  --name client-container \  # Assign a name to the container
  client-image  # Use the built client container image
