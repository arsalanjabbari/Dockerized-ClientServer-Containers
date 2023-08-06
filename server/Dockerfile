# Use the latest official Ubuntu image as the base
FROM ubuntu:latest

# Install required packages
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install Python dependencies
COPY ./requirements.txt .
RUN pip3 install -r ./requirements.txt

# Copy the server code into the container
COPY server.py .

# Expose the server port (assuming your server listens on port 8000)
EXPOSE 8000

# Start the server application
CMD ["python3", "server.py"]
