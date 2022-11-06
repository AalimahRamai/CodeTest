from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required, current_identity


from App.controllers import (
    log_review,
    delete_review,
    view_student_reviews,
    view_user_reviews,
    like_review,
    dislike_review,
)

review_views = Blueprint('review_views', __name__, template_folder='../templates')

@review_views.route('/api/reviews', methods=['POST'])
@jwt_required()
def log_review_action():
    if get_user(current_identity.id):
        data = request.json
        result = log_review(data['userId'], data['studentId'], data['comment'])
        if result:
            return jsonify({'message': f"review from: {data['userId']} about: {data['studentId']} logged"}), 201
        return jsonify({"message": "Server error"}), 500
    return jsonify({"error": "User not authorized to perform this action"}), 403

@review_views.route('/api/reviews', methods=['GET'])
@jwt_required()
def view_student_reviews_action():
    if get_user(current_identity.id):
        data = request.json
        reviews = view_student_reviews(data['studentId'])
        if reviews:
            return jsonify(reviews)
        return jsonify({"error": f"No reviews on {data['studentId']} found"}), 404
    return jsonify({"error": "User not authorized to perform this action"}), 403

        
@review_views.route('/api/reviews', methods=['GET'])
@jwt_required()
def view_user_reviews_action():
    if get_user(current_identity.id):
        data = request.json
        reviews = view_user_reviews(data['userId'])
        if reviews:
            return jsonify(reviews)
        return jsonify({"error": f"No reviews written by {data['userId']} found"}), 404
    return jsonify({"error": "User not authorized to perform this action"}), 403
        

@review_views.route('/api/reviews/<reviewId>/<userId>/<studentId>', methods=['PUT'])
@jwt_required()
def like_review_action(reviewId, userId, studentId):
    if get_user(current_identity.id):
        #data = request.json
        result = like_review(reviewId, userId, studentId)
        if result:
            return jsonify({'message': f"review about student {studentId} liked"}), 201
        return jsonify({"message": "Server error"}), 500
    return jsonify({"error": "User not authorized to perform this action"}), 403
    
@review_views.route('/api/reviews/<reviewId>/<userId>/<studentId>', methods=['PUT'])
@jwt_required()
def dislike_review_action(reviewId, userId, studentId):
    if get_user(current_identity.id):
        #data = request.json
        result = dislike_review(reviewId, userId, studentId)
        if result:
            return jsonify({'message': f"review about student {studentId} disliked"}), 201
        return jsonify({"message": "Server error"}), 500
    return jsonify({"error": "User not authorized to perform this action"}), 403
