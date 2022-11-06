import os, tempfile, pytest, logging, unittest
from werkzeug.security import check_password_hash, generate_password_hash

from App.main import create_app
from App.database import create_db
from App.models import User
from App.controllers import (
    create_user,
    get_all_users_json,
    authenticate,
    get_user,
    get_user_by_username,
    update_user,
    add_student,
    get_all_students,
    get_all_students_json,
    update_student,
    log_review, 
    get_review,
    view_student_reviews,
    view_user_reviews,
    like_review,
    dislike_review,
)

from wsgi import app


LOGGER = logging.getLogger(__name__)

'''
   Unit Tests
'''
class UserUnitTests(unittest.TestCase):

    def test_new_user(self):
        user = User("allisonHarper127", "allie127", "Allison", "Harper", "Lecturer")
        assert user.username == "allisonHarper127"

    # pure function no side effects or integrations called
    def test_toJSON(self):
        user = User("allisonHarper127", "allie127", "Allison", "Harper", "Lecturer")
        user_json = user.toJSON()
        self.assertDictEqual(user_json, {"id":None, "username":"allisonHarper127", "firstName":"Allison", "lastName":"Harper", "jobTitle":"Lecturer"})

    
    def test_hashed_password(self):
        password = "allie127"
        hashed = generate_password_hash(password, method='sha256')
        user = User("allisonHarper127", password, "Allison", "Harper", "teacher")
        assert user.password != password

    def test_check_password(self):
        password = "allie127"
        user = User("allisonHarper127", password, "Allison", "Harper", "teacher")
        assert user.check_password(password)

    def test_new_Student(self):
        student = Student("David", "Moriarty", "FST", "Computer Science", 3)
        assert student.firstName == "David"
    
    def test_new_review(self):
        review = review("Unable to focus")
        assert review.comment =="Unable to focus"

'''
    Integration Tests
'''

# This fixture creates an empty database for the test and deletes it after the test
# scope="class" would execute the fixture once and resued for all methods in the class
@pytest.fixture(autouse=True, scope="module")
def empty_db():
    app.config.update({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db'})
    create_db(app)
    yield app.test_client()
    os.unlink(os.getcwd()+'/App/test.db')


def test_authenticate():
    user = create_user("bob", "bobpass", "Bob", "Duncan", "Lecturer")
    assert authenticate("bob", "bobpass", "Bob", "Duncan", "Lecturer") != None

class UsersIntegrationTests(unittest.TestCase):

    def test_create_user(self):
        user = create_user("rick", "rickpass", "Rick", "Bass", "Tutor")
        assert user.username == "rick", user.firstName=="Rick", user.lastName=="Bass", user.jobTitle=="Tutor"

    def test_get_all_users_json(self):
        users_json = get_all_users_json()
        self.assertListEqual([{"id":1, "username":"bob", "firstName":"Bob", "lastName":"Duncan", "jobTitle":"Lecturer"}, {"id":2, "username":"rick", "firstName":"Rick", "lastName":"Bass", "jobTitle":"Tutor"}], users_json)

    # Tests data changes in the database
    def test_update_user(self):
        update_user(1, "ronnie", "Ronnie", "Brown", "Lecturer")
        user = get_user(1)
        assert user.username == "ronnie", user.firstName == "Ronnie", user.lastName == "Brown"

    def test_add_student(self):
        student = add_student("Brandon", "Pope", "Science&Technology", "BscComputer Science", "full-time", "Year1")
        assert student.firstName == "Brandon", student.lastName == "Pope", student.faculty == "Science&Technology", student.degree == "BscComputerScience", student.status == "full-time", student.courseLevel == "Year1"
    
    def test_get_all_students_json(self):
        students_json = get_all_students_json()
        self.assertListEqual([{"id":1, "firstName":"Brandon", "lastName":"Pope", "faculty":"Science&Technology", "degree":"BscComputerScience", "status":"full-time", "courseLevel":"Year1"}], students_json)

    # Tests data changes in the database
    def test_update_student(self):
        update_student(1, "Crystal", "Fletcher", "Science&Technology", "BscInformationTechnology", "part-time", "Year2")
        student = search_student(1)
        assert student.firstName == "Crystal", student.lastName == "Fletcher", student.faculty == "Science&Technology", student.degree=="BscInformationTechnology", student.status=="part-time", student.courseLevel=="Year2"

    def test_log_review(self):
        review = log_review(1, 1, "Always absent from lectures and tutorials")
        assert review.userId == 1, review.studentId==1, review.comment=="Always absent from lectures and tutorials"

    def test_student_reviews_json(self):
        reviews_json = view_student_reviews(1)
        self.assertListEqual([{"userId":1, "studentId": 1, "comment":"Always absent from lectures and tutorials"}], reviews_json)

    def test_user_reviews_json(self):
        reviews_json = view_user_reviews(1)
        self.assertListEqual([{"userId":1, "studentId": 1, "comment":"Always absent from lectures and tutorials"}], reviews_json)

    def test_like_review(self):
        review = like_review(1, 1, 1)
        assert review.like == True

    def test_dislike_review(self):
        review = dislike_review(1, 1, 1)
        assert review.dislike == True    
    
