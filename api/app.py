from flask import Flask, request, jsonify
from pymongo import MongoClient
from pymongo.errors import PyMongoError
from bson import ObjectId

app = Flask(__name__)

# Configure the MongoDB connection URI
uri = 'mongodb+srv://AbdulHadi:khizer007@bigdata.jkwutqo.mongodb.net/test?retryWrites=true&w=majority'
@app.route('/')
def index():
    return "Hello, Flask World!"

if __name__ == '__main__':
    app.run(debug=True)
