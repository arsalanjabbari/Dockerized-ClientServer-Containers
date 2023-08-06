#!/bin/bash

# This script opens an interactive shell session within the running client container.
# Ensure that the 'fileclient.sh' script is already running before using this.

# Check if the 'fileclient.sh' script is running
if sudo docker ps | grep -q "client-container"; then
  # If the client container is running, open an interactive shell session within it
  sudo docker exec -it client-container bash
else
  echo "The 'fileclient.sh' script is not running. Please start it before using this script."
fi
