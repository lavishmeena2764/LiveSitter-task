from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for React frontend

app.config['MONGO_URI'] = "mongodb://localhost:27017/overlays_db"
mongo = PyMongo(app)
db = mongo.db

@app.route('/', methods=['GET'])
def welcome():
    return jsonify({"message":"Hello User"}), 200


@app.route('/overlays', methods=['POST'])
def create_overlay():
    data = request.json
    overlay = {
        'content': data['content'],
        'position': data['position'],
        'size': data['size']
    }
    overlay_id = db.overlays.insert_one(overlay).inserted_id
    return jsonify({'id': str(overlay_id)}), 201

@app.route('/overlays', methods=['GET'])
def get_overlays():
    overlays = []
    for overlay in db.overlays.find():
        overlays.append({
            'id': str(overlay['_id']),
            'content': overlay['content'],
            'position': overlay['position'],
            'size': overlay['size']
        })
    return jsonify(overlays), 200

@app.route('/overlays/<id>', methods=['PUT'])
def update_overlay(id):
    data = request.json
    db.overlays.update_one({'_id': ObjectId(id)}, {'$set': {
        'content': data['content'],
        'position': data['position'],
        'size': data['size']
    }})
    return jsonify({'msg': 'Overlay updated'}), 200

@app.route('/overlays/<id>', methods=['DELETE'])
def delete_overlay(id):
    db.overlays.delete_one({'_id': ObjectId(id)})
    return jsonify({'msg': 'Overlay deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)
