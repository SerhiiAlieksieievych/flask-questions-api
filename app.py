from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('questions.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/questions', methods=['GET'])
def get_questions():
    conn = get_db_connection()
    questions = conn.execute('SELECT * FROM questions').fetchall()
    conn.close()

    result = []
    for q in questions:
        result.append({
            "id": q["id"],
            "question": q["question"],
            "options": [q["option_a"], q["option_b"], q["option_c"], q["option_d"]]
        })
    return jsonify(result)

@app.route('/answer', methods=['POST'])
def check_answer():
    data = request.get_json()
    question_id = data.get('question_id')
    user_answer = data.get('user_answer')

    conn = get_db_connection()
    question = conn.execute('SELECT answer FROM questions WHERE id = ?', (question_id,)).fetchone()
    conn.close()

    if question is None:
        return jsonify({"error": "Питання не знайдено"}), 404

    correct = (user_answer.strip().lower() == question['answer'].strip().lower())
    return jsonify({"correct": correct})

if __name__ == '__main__':
    app.run(debug=True)
