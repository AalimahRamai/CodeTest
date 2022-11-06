from App.database import db

class Review(db.Model):

    reviewId = db.Column(db.Integer, primary_key=True, nullable=False) 
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))
    studentId = db.Column(db.Integer, db.ForeignKey('student.studentId'))
    comment = db.Column(db.String)
    like = db.Column(db.Boolean)
    dislike = db.Column(db.Boolean)
    
    
    def __init__(self, userId, studentId, comment):
        self.userId = userId
        self.studentId = studentId
        self.comment = comment
        self.like = like
        self.dislike = dislike
        
    def __repr__(self):
        return f'<Review {self.comment} written by: {self.user.username} {self.user.jobTitle} about: {self.studentId} {self.student.firstName} {self.student.lastName}>'

    def toJSON(self):
        return{
            'reviewId': self.reviewId,
            'userId': self.userId,
            'studentId': self.studentId,
            'comment': self.comment,
            'like': self.like,
            'dislike': self.dislike
        }

    def set_like(self):
        """Set like field to false"""
        self.like = False

    def set_dislike(self):
        """Set dislike field to false"""
        self.like = False
