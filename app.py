import sqlite3
from flask import Flask, jsonify, request
import jwt
from datetime import datetime, timedelta

app = Flask(__name__)

DATABASE = 'keys.db'

# Create and connect to the SQLite database
def get_db():
    db = sqlite3.connect(DATABASE)
    return db

# Generate an RSA key (simplified for demonstration)
def generate_rsa_key():
    # Normally, you'd use a library like cryptography to generate a key
    # For this example, let's return a dummy key
    return "Dummy_RSA_Private_Key"

@app.route('/generate-key', methods=['POST'])
def generate_key():
    key = generate_rsa_key()
    timestamp = datetime.now()
    
    db = get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO keys (key, timestamp) VALUES (?, ?)", (key, timestamp))
    db.commit()
    db.close()
    
    return jsonify({"message": "Key generated and saved!"})

@app.route('/save-key', methods=['POST'])
def save_key():
    key = request.json['key']
    timestamp = datetime.now()
    
    db = get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO keys (key, timestamp) VALUES (?, ?)", (key, timestamp))
    db.commit()
    db.close()
    
    return jsonify({"message": "Key saved!"})

@app.route('/fetch-key', methods=['GET'])
def fetch_key():
    expired = request.args.get('expired', default = None)
    current_time = datetime.now()
    
    db = get_db()
    cursor = db.cursor()
    
    if expired:
        # Fetch a key that was saved more than an hour ago
        hour_ago = current_time - timedelta(hours=1)
        cursor.execute("SELECT key FROM keys WHERE timestamp < ?", (hour_ago,))
    else:
        # Fetch the most recent key
        cursor.execute("SELECT key FROM keys ORDER BY timestamp DESC LIMIT 1")
    
    key = cursor.fetchone()
    db.close()
    
    if not key:
        return jsonify({"message": "No key found!"}), 404

    # Generate a JWT as a demonstration
    token = jwt.encode({"key": key[0], "exp": current_time + timedelta(hours=1)}, key[0], algorithm="HS256")

    return jsonify({"key": key[0], "token": token})

if __name__ == '__main__':
    app.run(debug=True)
