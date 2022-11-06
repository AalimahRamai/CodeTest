from App.models import User, Student, Review
from App.database import db

def add_student(firstName, lastName, faculty, degree, status, courselevel):
    newstudent = Student(firstName=firstName, lastName=lastName, faculty=faculty, degree=degree, status=status, courseLevel=courseLevel)
    db.session.add(newstudent)
    db.session.commit()
    return newstudent

def search_student(studentId):
    return Student.query.get(studentId)

def get_all_students():
    return Student.query.all()

def get_Karma_Score(studentId):
    student = search_student(studentId)
    if student:
        return student.toJSON()
    return None

def get_all_students_json():
    students = Student.query.all()
    if not students:
        return []
    students = [student.toJSON() for student in students]
    return students

def update_student(studentId, firstName, lastName, faculty, degree, status, courselevel):
    student = search_student(studentId)
    if student:
            student.firstName = firstName
            student.lastName = lastName
            student.faculty = faculty
            student.degree = degree
            student.status =status
            student.courseLevel = courseLevel
            db.session.add(student)
            return db.session.commit()
    return None

"""
def add_Student(studentId, student_firstName, student_lastName, student_faculty, student_degree, student_courseLevel, reviews):
    new_student = Student(studentId=studentId, student_firstName=student_firstName, student_lastName=student_lastName, student_faculty=student_faculty, student_degree=student_degree, student_courseLevel=student_courseLevel, reviews=reviews)
    db.session.add(new_student)
    db.session.commit()
    return new_review
def get_student(studentId):
    return User.query.get(studentId)
def update_student(studentId, student_firstName, student_lastName, student_faculty, student_degree, student_courseLevel, reviews):
    student = get_student(studentId):
    if student:
        student.studentId = studentId
        student.student_firstName = student_firstName
        student.student_lastName = student_lastName
        student.student_faculty = student_faculty
        student.student_degree = student_degree
        student.reviews = reviews
        db.session.add(student)
        return db.session.commit()
    return None
"""
