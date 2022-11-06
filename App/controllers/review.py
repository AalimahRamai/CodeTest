from App.models import User, Student, Review
from App.database import db

def log_review(userId, studentId, comment):
    student = Student.query.get(studentId=studentId)
    if student:
        review = Review(userId=userId, studentId=studentId, comment=comment, like=like)
        db.session.add(review)
        db.session.commit()
        return review
    return False

def delete_review(reviewId, userId, studentId):
    review = Review.query.filter(reviewId=reviewId, userId=userId, studentId=student)
    if review:
        db.session.delete(review)
        res = db.session.commit()
        return res
    return False
             

def get_review(id):
    return Review.query.get(id)
    
def view_student_reviews(studentId): #view all the reviews about a particular student
    reviews = Review.query.filter(studentId=studentId).all()
    if not reviews:
        return []
    reviews = [review.toJSON() for review in reviews]
    return reviews

def view_user_reviews(userId): #a user can view all the reviews made by themselves
    reviews = Review.query.filter(userId=userId).all()
    if not reviews:
        return []
    reviews = [review.toJSON() for review in reviews]
    return reviews

def like_review(reviewId, userId, studentId):
    review = Review.query.filter(reviewId=reviewId, userId=userId, studentId=studentId)
    if review:
        review.like = True
        db.session.add(review)
        db.session.commit()
        return review
    return False

def dislike_review(reviewId, userId, studentId):
    review = Review.query.filter(reviewId=reviewId, userId=userId, studentId=studentId)
    if review:
        review.dislike = True
        db.session.add(review)
        db.session.commit()
        return review
    return False  
