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
# Create a PyMongo instance
client = MongoClient(uri)

# Select the database and collection
db = client.get_database("BigData")
collection = db.get_collection("Users")
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


@app.route('/process_data', methods=['POST'])
def process_data():
    try:
        data = request.get_json()
        print("Received JSON data:", data)

        # Retrieve data fields
        name = data.get('name')
        age = data.get('age')
        number = data.get('number')
        print(f"Received data - Name: {name}, Age: {age}, Number: {number}")

        # Construct MongoDB record
        record = {
            'name': name,
            'age': age,
            'number': number
        }
        print("Constructed Record:", record)
        # Insert data into MongoDB
        result = collection.insert_one(record)

        return jsonify({"result": "Success: Data inserted into MongoDB!", "inserted_id": str(result.inserted_id)})
    except PyMongoError as e:
        return jsonify({"result": f"Failure: {str(e)}"})
@app.route('/search_user', methods=['GET'])
def search_user():
    name = request.json.get('name')

    # Connect to MongoDB
    db = client.BigData.Users  # Replace 'your_collection' with your MongoDB collection name

    # Search for the user by name
    user = db.find_one({'name': name})

    if user:
        # Convert ObjectId to string
        user['_id'] = str(user['_id'])

        return jsonify({"result": "Success: User found!", "user": user})
    else:
        return jsonify({"result": "Error: User not found."})

if __name__ == '__main__':
    app.run(debug=True)
