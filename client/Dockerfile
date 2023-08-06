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
RUN pip3 install -r requirements.txt

# Copy the client code into the container
COPY client.py .

# Start the client application with appropriate arguments (replace 'server-container' and '8000' with your values)
CMD ["python3", "client.py", "server-container", "8000"]
