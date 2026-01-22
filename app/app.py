from flask import Flask, request, jsonify
from data import get_all_students, add_student_to_db
from datetime import datetime

app = Flask(__name__)

@app.route('/students', methods=['GET'])
def list_students():
    students = get_all_students()
    output = []
    for s in students:
        output.append({
            "id": s.id, 
            "name": s.name, 
            "email": s.email, 
            "course": s.course, 
            "gpa": s.gpa,
            "joined": s.created_at
        })
    return jsonify(output)

@app.route('/students', methods=['POST'])
def create_student():
    data = request.json
    # Business Logic: Validation
    if "@" not in data.get('email', ''):
        return jsonify({"error": "Invalid email format"}), 400
    
    add_student_to_db(
        data['name'], 
        data['email'], 
        data.get('course', 'General'), 
        data.get('gpa', 0.0)
    )
    return jsonify({"message": "Student record created"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
