from App.database import db

class Student(db.Model):
    studentId = db.Column(db.Integer, nullable=False, primary_key=True)
    firstName = db.Column(db.String, nullable=False)
    lastName = db.Column(db.String, nullable=False)
    faculty = db.Column(db.String)
    degree = db.Column(db.String)
    status = db.Column(db.String)
    courseLevel = db.Column(db.String)
    reviews = db.relationship('Review', backref=db.backref('student', lazy='joined'))
    
    def __init__(self, firstName, lastName, faculty, degree, status, courseLevel):
        self.firstName = firstName
        self.lastName = lastName
        self.faculty = faculty
        self.degree = degree
        self.status = status
        self.courseLevel = courseLevel
    
    def __repr__(self):
        return f'<Student {self.studentId} {self.firstName} {self.lastName} {self.faculty} {self.degree} {self.status} {self.courseLevel}>'


    def toJSON(self):
        return{
            'studentId': self.studentId,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'faculty': self.faculty,
            'degree': self.degree,
            'status': self.status,
            'courseLevel': self.courseLevel,
            'karmaScore': self.getKarmaScore()
        }


    def getKarmaScore(self):
        numLikes = 0
        numDislikes =0
        score = 0
        for review in self.reviews:
            if review.like:
                numLikes += 1

            if review.dislike:
                numDislikes +=1
        total = numDislikes + numLikes
        score = (numLikes - numDislikes/total)*100
        return 
