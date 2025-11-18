from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for users
users = {}
user_id_counter = 1

# Root endpoint
@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to User Management API",
        "endpoints": {
            "GET /users": "Get all users",
            "GET /users/<id>": "Get user by ID",
            "POST /users": "Create a new user",
            "PUT /users/<id>": "Update user by ID",
            "DELETE /users/<id>": "Delete user by ID"
        }
    })

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({
        "success": True,
        "count": len(users),
        "users": list(users.values())
    }), 200

# GET user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify({
            "success": True,
            "user": user
        }), 200
    return jsonify({
        "success": False,
        "error": "User not found"
    }), 404

# POST - Create new user
@app.route('/users', methods=['POST'])
def create_user():
    global user_id_counter
    
    data = request.json
    
    # Validate required fields
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({
            "success": False,
            "error": "Name and email are required"
        }), 400
    
    # Create new user
    new_user = {
        "id": user_id_counter,
        "name": data['name'],
        "email": data['email'],
        "age": data.get('age', None)
    }
    
    users[user_id_counter] = new_user
    user_id_counter += 1
    
    return jsonify({
        "success": True,
        "message": "User created successfully",
        "user": new_user
    }), 201

# PUT - Update user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = users.get(user_id)
    
    if not user:
        return jsonify({
            "success": False,
            "error": "User not found"
        }), 404
    
    data = request.json
    
    if not data:
        return jsonify({
            "success": False,
            "error": "No data provided"
        }), 400
    
    # Update user fields
    if 'name' in data:
        user['name'] = data['name']
    if 'email' in data:
        user['email'] = data['email']
    if 'age' in data:
        user['age'] = data['age']
    
    users[user_id] = user
    
    return jsonify({
        "success": True,
        "message": "User updated successfully",
        "user": user
    }), 200

# DELETE user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = users.get(user_id)
    
    if not user:
        return jsonify({
            "success": False,
            "error": "User not found"
        }), 404
    
    del users[user_id]
    
    return jsonify({
        "success": True,
        "message": "User deleted successfully"
    }), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)