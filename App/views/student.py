from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required, current_identity


from App.controllers import (
    add_student, 
    search_student,
    update_student,
    get_all_students,
    get_all_students_json,
)
    
student_views = Blueprint('student_views', __name__, template_folder='../templates')

@student_views.route('/api/students', methods=['POST'])
@jwt_required()
def add_student_action():
    if get_user(current_identity.id):
        data = request.json
        result = add_student(data['firstName'], data['lastName'], data['faculty'], data['degree'], data['status'], data['courseLevel'] )
        if result:
            return jsonify({'message': f"student {data['firstName'], data['lastName']} added"}), 201
        return jsonify({"message": "Server error"}), 500
    return jsonify({"error": "User not authorized to perform this action"}), 403

@student_views.route('/api/students', methods=['GET'])
@jwt_required()
def get_students_action():
    if get_user(current_identity.id):
        students = get_all_students_json()
        return jsonify(students)
    return jsonify({"error": "User not authorized to perform this action"}), 403

    
@student_views.route('/api/students', methods=['GET'])
def search_student_action():
    data = request.json
    student = search_student(data["studentId"])
    if student:
        return jsonify(student.toJSON)
    return jsonify({"error": f"Student with id {studentId} not found"}), 404

@student_views.route('/api/students/<studentId>', methods=['PUT'])
@jwt_required()
def update_student_action(studentId):
    if get_user(current_identity.id):
        data = request.json
        student = update_student(studentId, data['firstName'], data['lastName'], data['faculty'], data['degree'], data['status'], data['courseLevel'] )
        if student:
            return jsonify(student)
        return jsonify({"error": f"Student id {studentId} not found"}), 404
    return jsonify({"error": "User not authorized to perform this action"}), 403
