# Dockerized Client-Server Containers

This repository contains the code and instructions for an introductory project on Dockerization. Explore the world of containerization as you build and depoly simple client and server containers using Docker. Follow along with the provided guide to get started and learn how to dockerize applications effectively.

## Table of Contents
- [Introduction](#introduction)
- [Project Overview](#project-overview)
- [Features](#features)
- [Getting Started](#getting-started)
- [Conclusion](#conclusion)

## Introduction

Welcome to the Dockerized Client-Server Containers project repository! This repository is designed to provide you with the necessary code and instructions to explore the world of Docker containerization. In this project, you'll learn how to build and deploy simple client and server containers using Docker, enabling you to effectively manage and distribute applications within isolated environments.

## Project Overview

In this project, we have organized the code and resources into the following structure:

### `client/`

This directory contains the code and files related to the client container.

- `client.py`: The main Python script for the client application.
- `Dockerfile`: The Dockerfile used to build the client container image.
- `requirements.txt`: A list of Python dependencies required by the client application.

### `server/`

This directory contains the code and files related to the server container.

- `server.py`: The main Python script for the server application.
- `Dockerfile`: The Dockerfile used to build the server container image.
- `requirements.txt`: A list of Python dependencies required by the server application.

### `docker-compose.yml`

The `docker-compose.yml` file defines the services, networks, and volumes for the Docker containers. It allows you to easily manage the deployment of both the client and server containers as a unified application.

### Shell Scripts

- `fileclient.sh`: A shell script that provides functionality to interact with the client container, including copying files into the container.
- `fileserver.sh`: A shell script that provides functionality to interact with the server container, including copying files into the container.
- `open-client-shell.sh`: A shell script to open a shell within the client container for manual interaction and testing.

## Features

- **Client-Server Interaction:** Experience a client-server architecture where the client interacts with the server through REST APIs.
- **Docker Containerization:** Learn how to containerize applications using Docker, enabling easy deployment and isolation.
- **File Transfer:** Explore file transfer between the client and server containers, including checksum verification.
- **REST API:** Use a simple REST API to insert, retrieve, and delete person records from the server.
- **Data Persistence:** Store person records in a MongoDB container for data persistence.
- **Automated Scripts:** Convenient shell scripts provided for common tasks like copying files and opening a client shell.

## Getting Started

To get started with this project, follow these steps:

1. Clone this repository to your local machine.
2. Navigate to the project directory.

### Building and Running Containers

3. Navigate to the `client/` directory and build the client container image:
   ```
   cd client
   docker build -t client-container .
   ```

4. Navigate to the `server/` directory and build the server container image:
   ```
   cd ../server
   docker build -t server-container .
   ```

5. Return to the project directory and start the containers using `docker-compose`:
   ```
   cd ..
   docker-compose up -d
   ```

### Interacting with Containers

6. Use the provided shell scripts for interacting with the containers:
   - To copy a file into the client container: `./fileclient.sh yourfile.txt`
   - To copy a file into the server container: `./fileserver.sh yourfile.txt`
   - To open a shell within the client container: `./open-client-shell.sh`

## Conclusion

Congratulations! You've successfully set up and deployed the Dockerized Client-Server Containers project. Feel free to explore, modify, and experiment with the code and containers to gain a deeper understanding of Docker containerization. For more advanced usage and concepts, consider diving into Docker's documentation.

If you have any questions or run into issues, please refer to the provided documentation or seek help from the community.

Happy Dockerizing! 🐳