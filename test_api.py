import requests
import json

BASE_URL = "http://localhost:5000"

def print_response(response, operation):
    print(f"\n{'='*50}")
    print(f"Operation: {operation}")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print(f"{'='*50}")

def test_api():
    print("🚀 Starting API Tests...")
    
    # Test 1: GET all users (empty)
    print("\n1️⃣ Testing GET all users (should be empty)")
    response = requests.get(f"{BASE_URL}/users")
    print_response(response, "GET /users")
    
    # Test 2: POST create user 1
    print("\n2️⃣ Testing POST - Create User 1")
    user1_data = {
        "name": "Alice Smith",
        "email": "alice@example.com",
        "age": 28
    }
    response = requests.post(f"{BASE_URL}/users", json=user1_data)
    print_response(response, "POST /users")
    user1_id = response.json()['user']['id']
    
    # Test 3: POST create user 2
    print("\n3️⃣ Testing POST - Create User 2")
    user2_data = {
        "name": "Bob Johnson",
        "email": "bob@example.com",
        "age": 32
    }
    response = requests.post(f"{BASE_URL}/users", json=user2_data)
    print_response(response, "POST /users")
    
    # Test 4: POST create user 3
    print("\n4️⃣ Testing POST - Create User 3")
    user3_data = {
        "name": "Charlie Brown",
        "email": "charlie@example.com"
    }
    response = requests.post(f"{BASE_URL}/users", json=user3_data)
    print_response(response, "POST /users")
    
    # Test 5: GET all users (should have 3)
    print("\n5️⃣ Testing GET all users (should have 3)")
    response = requests.get(f"{BASE_URL}/users")
    print_response(response, "GET /users")
    
    # Test 6: GET specific user
    print(f"\n6️⃣ Testing GET user by ID (ID: {user1_id})")
    response = requests.get(f"{BASE_URL}/users/{user1_id}")
    print_response(response, f"GET /users/{user1_id}")
    
    # Test 7: PUT update user
    print(f"\n7️⃣ Testing PUT - Update User {user1_id}")
    update_data = {
        "name": "Alice Smith Updated",
        "email": "alice.updated@example.com",
        "age": 29
    }
    response = requests.put(f"{BASE_URL}/users/{user1_id}", json=update_data)
    print_response(response, f"PUT /users/{user1_id}")
    
    # Test 8: GET updated user
    print(f"\n8️⃣ Testing GET updated user (ID: {user1_id})")
    response = requests.get(f"{BASE_URL}/users/{user1_id}")
    print_response(response, f"GET /users/{user1_id}")
    
    # Test 9: DELETE user
    print(f"\n9️⃣ Testing DELETE user (ID: {user1_id})")
    response = requests.delete(f"{BASE_URL}/users/{user1_id}")
    print_response(response, f"DELETE /users/{user1_id}")
    
    # Test 10: GET all users (should have 2 left)
    print("\n🔟 Testing GET all users (should have 2 left)")
    response = requests.get(f"{BASE_URL}/users")
    print_response(response, "GET /users")
    
    # Test 11: GET non-existent user (404)
    print("\n1️⃣1️⃣ Testing GET non-existent user (should return 404)")
    response = requests.get(f"{BASE_URL}/users/999")
    print_response(response, "GET /users/999")
    
    # Test 12: POST with missing fields (400)
    print("\n1️⃣2️⃣ Testing POST with missing fields (should return 400)")
    bad_data = {"name": "Test User"}  # Missing email
    response = requests.post(f"{BASE_URL}/users", json=bad_data)
    print_response(response, "POST /users (bad request)")
    
    print("\n✅ All tests completed!")

if __name__ == "__main__":
    try:
        test_api()
    except requests.exceptions.ConnectionError:
        print("❌ Error: Could not connect to the server.")
        print("Make sure the Flask app is running on http://localhost:5000")
        print("Run: python app.py")