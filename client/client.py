import os
import sys
import time
import requests
import hashlib

# Retrieve host and port from command-line arguments
host = sys.argv[1]
port = sys.argv[2]

# Server URL
SERVER_URL = f'http://{host}:{port}'

# Directory and file information
CLIENT_DIR = '/clientdata'
FILE_NAME = 'file.txt'

# Create client directory if it doesn't exist
if not os.path.isdir(CLIENT_DIR):
    os.mkdir(CLIENT_DIR)


def get_checksum(file_path: str):
    """Calculate and return the MD5 checksum of a file."""
    with open(file_path, 'rb') as fp:
        file_hash = hashlib.md5()
        while chunk := fp.read(8192):
            file_hash.update(chunk)
    return file_hash.hexdigest()


def save_file(response):
    """Save a file received from the server and verify its checksum."""
    with open(f'{CLIENT_DIR}/{FILE_NAME}', 'wb') as f:
        f.write(response.content)
    print(f'File saved to {CLIENT_DIR}/{FILE_NAME}')

    # Calculate checksum of the received file and compare it with the server's checksum
    checksum = get_checksum(f'{CLIENT_DIR}/{FILE_NAME}')
    response_checksum = response.headers['X-Checksum']
    if checksum == response_checksum:
        print('Checksum verified successfully')
    else:
        print('Checksum verification failed')


def test_server():
    print('#### TESTING ####')

    # Insert sample persons and interact with the server
    person1 = insert_person('Sweeney', 'Todd')
    print('Inserted:', person1)

    person2 = insert_person('Edward', 'Scissorhands')
    print('Inserted:', person2)

    found = get_person(person2['personID'])
    print('Found:', found)

    all_persons = get_persons()
    print('All:', all_persons)

    delete_person(person1['personID'])
    delete_person(person2['personID'])

    all_persons = get_persons()
    print('All:', all_persons)

    get_file()


if __name__ == "__main__":
    test_server()

    # Keep the client running (optional)
    while True:
        time.sleep(5)
