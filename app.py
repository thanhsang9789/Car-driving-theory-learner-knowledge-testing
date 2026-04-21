from flask import Flask, render_template, jsonify, request, send_from_directory, session
import json
import os
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this' # Change this to a real secret key

DATABASE = 'database.db'

def get_db():
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db

def init_db():
    with app.app_context():
        db = get_db()
        # Create users table
        db.execute('''CREATE TABLE IF NOT EXISTS users 
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                       email TEXT UNIQUE NOT NULL, 
                       password TEXT NOT NULL)''')
        # Create history table
        db.execute('''CREATE TABLE IF NOT EXISTS history 
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                       user_id INTEGER NOT NULL, 
                       question_id INTEGER NOT NULL, 
                       question_text TEXT, 
                       correct_answer TEXT, 
                       is_correct BOOLEAN, 
                       date TEXT,
                       FOREIGN KEY (user_id) REFERENCES users (id))''')
        db.commit()

init_db()

# Load questions from JSON
def load_questions():
    json_path = os.path.join(os.path.dirname(__file__), 'questions.json')
    if os.path.exists(json_path):
        with open(json_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/questions.json')
def serve_questions_json():
    return send_from_directory(os.path.dirname(__file__), 'questions.json')

@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    
    if not email or not password:
        return jsonify({"error": "Missing email or password"}), 400
    
    hashed_password = generate_password_hash(password)
    
    db = get_db()
    try:
        db.execute('INSERT INTO users (email, password) VALUES (?, ?)', (email, hashed_password))
        db.commit()
        return jsonify({"message": "User registered successfully"})
    except sqlite3.IntegrityError:
        return jsonify({"error": "Email already exists"}), 400

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    
    db = get_db()
    user = db.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()
    
    if user and check_password_hash(user['password'], password):
        session['user_id'] = user['id']
        session['user_email'] = user['email']
        return jsonify({"message": "Logged in successfully", "email": user['email']})
    
    return jsonify({"error": "Invalid email or password"}), 401

@app.route('/api/logout')
def logout():
    session.clear()
    return jsonify({"message": "Logged out successfully"})

@app.route('/api/user_info')
def user_info():
    if 'user_id' in session:
        return jsonify({"logged_in": True, "email": session['user_email']})
    return jsonify({"logged_in": False})

@app.route('/api/history', methods=['GET', 'POST'])
def handle_history():
    if 'user_id' not in session:
        return jsonify({"error": "Not logged in"}), 401
    
    db = get_db()
    user_id = session['user_id']
    
    if request.method == 'POST':
        data = request.json
        db.execute('''INSERT INTO history 
                      (user_id, question_id, question_text, correct_answer, is_correct, date) 
                      VALUES (?, ?, ?, ?, ?, ?)''', 
                   (user_id, data['id'], data['q'], data['a'], data['is_correct'], data['date']))
        db.commit()
        return jsonify({"message": "History saved"})
    
    # GET history
    history = db.execute('SELECT * FROM history WHERE user_id = ? ORDER BY id DESC', (user_id,)).fetchall()
    return jsonify([dict(h) for h in history])

@app.route('/api/questions')
def get_questions():
    questions = load_questions()
    client_questions = []
    for q in questions:
        client_questions.append({
            "id": q["id"],
            "question": q["q"],
            "options": [opt["t"] for opt in q["opts"]],
            "category": q.get("cn", "General"),
            "is_critical": q.get("crit", False)
        })
    return jsonify(client_questions)

@app.route('/api/check_answer', methods=['POST'])
def check_answer():
    data = request.json
    question_id = data.get('id')
    user_answer_idx = data.get('answer_idx')
    
    questions = load_questions()
    for q in questions:
        if q["id"] == question_id:
            correct_idx = q["ans"] - 1
            is_correct = correct_idx == user_answer_idx
            return jsonify({
                "correct": is_correct,
                "correct_answer_idx": correct_idx,
                "explanation": q.get("tip", "")
            })
            
    return jsonify({"error": "Question not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
