import os
import random
import string
import hashlib

from bson import ObjectId
from flask import Flask, jsonify, request, send_from_directory, make_response
from pymongo import MongoClient
from pymongo.collection import Collection

app = Flask(__name__)

# Connect to the MongoDB container
mongo_client = MongoClient('mongo-container', 27017)
db = mongo_client['mydb']
person_collection: Collection = db['Person']

# Create directory for server data
SERVER_DIR = '/serverdata'
FILE_NAME = 'file.txt'
if not os.path.isdir(SERVER_DIR):
    os.mkdir(SERVER_DIR)

def random_text(size: int):
    """Generate and return random text of given size."""
    return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=size))

def create_file():
    """Create a file with random text data."""
    text = random_text(1024)
    with open(f'{SERVER_DIR}/{FILE_NAME}', 'w') as fp:
        fp.write(text)

def get_checksum(file_path: str):
    """Calculate and return the MD5 checksum of a file."""
    with open(file_path, 'rb') as fp:
        file_hash = hashlib.md5()
        while chunk := fp.read(8192):
            file_hash.update(chunk)
    return file_hash.hexdigest()

# REST API
@app.route('/persons', methods=['POST'])
def insert_person():
    data = request.get_json()
    name = data['name']
    family = data['family']
    inserted = person_collection.insert_one(dict(name=name, family=family))
    return jsonify(status='success', personID=str(inserted.inserted_id))

@app.route('/persons', methods=['GET'])
def get_persons():
    cursor = person_collection.find({})
    result = [dict(name=doc['name'], family=doc['family'], ID=str(doc['_id'])) for doc in cursor]
    return jsonify(result)

@app.route('/persons/<id>', methods=['GET'])
def get_person(id: str):
    result = person_collection.find_one({'_id': ObjectId(id)})
    if result is None:
        return jsonify(status='error', message='Person not found'), 404
    result['ID'] = str(result.pop('_id'))
    return jsonify(result)

@app.route('/persons/<id>', methods=['DELETE'])
def delete_person(id):
    result = person_collection.delete_one({'_id': ObjectId(id)})
    if result.deleted_count == 0:
        return jsonify(status='error', message='Person not found'), 404
    return jsonify(status='success', message='Person deleted successfully')

@app.route('/file', methods=['GET'])
def get_file():
    create_file()
    checksum = get_checksum(f'{SERVER_DIR}/{FILE_NAME}')
    response = make_response(send_from_directory(SERVER_DIR, FILE_NAME, as_attachment=True))
    response.headers['Content-Disposition'] = f'attachment; filename={FILE_NAME}'
    response.headers['X-Checksum'] = checksum
    return response

if __name__ == '__main__':
    # Start the server
    app.run(host='0.0.0.0', port=8000, debug=True)
