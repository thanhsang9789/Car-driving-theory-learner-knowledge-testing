from flask import Flask, render_template, jsonify, request, send_from_directory
import json
import os

app = Flask(__name__)

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

@app.route('/api/questions')
def get_questions():
    questions = load_questions()
    # Don't send the answers to the client, only questions and options
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
    user_answer_idx = data.get('answer_idx') # 0-indexed from frontend
    
    questions = load_questions()
    for q in questions:
        if q["id"] == question_id:
            # q["ans"] is 1-indexed
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
