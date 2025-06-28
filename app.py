from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory list to store users
users = [
    {"id": 1, "Name": "Rammohan", "email": "ram@gmail.com"},
    {"id": 2, "Name": "Harsha", "email": "harsha@gmail.com"}
]

# Home route
@app.route('/')
def home():
    return "Welcome to User Management API", 200

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# GET user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user), 200
    return jsonify({"Error": "User not found"}), 404

# POST create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()

    # Basic validation
    if not data or "Name" not in data or "email" not in data:
        return jsonify({"Error": "Name and email are required"}), 400

    new_user = {
        "id": users[-1]["id"] + 1 if users else 1,
        "Name": data["Name"],
        "email": data["email"]
    }
    users.append(new_user)
    return jsonify(new_user), 201

# PUT update existing user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        data = request.get_json()
        user["Name"] = data.get("Name", user["Name"])
        user["email"] = data.get("email", user["email"])
        return jsonify(user), 200
    return jsonify({"Error": "User not found"}), 404

# DELETE user by ID
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [u for u in users if u["id"] != user_id]
    return jsonify({"message": "User deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
