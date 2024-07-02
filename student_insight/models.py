from student_insight import db,login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    if 'ADM' == user_id[0:3]:
        id =  Admin.query.filter_by(id = user_id)[0].s_no
        user = Admin.query.get(id)
        return user
    else:
        id =  Student.query.filter_by(id = user_id)[0].s_no
        user = Student.query.get(id)
        return user


class Student(db.Model,UserMixin):
    s_no = db.Column(db.Integer(),primary_key = True)
    id = db.Column(db.String(10),unique =True,nullable = False)
    name = db.Column(db.String(25), nullable = False)
    dob = db.Column(db.String(10),nullable = False)
    cgpa=db.Column(db.Numeric(precision=8, asdecimal=False, decimal_return_scale=None), default = 0.0)
    fname=db.Column(db.String(25), nullable = False)
    mob=db.Column(db.Integer(),nullable = False)
    fmob=db.Column(db.Integer(),nullable = False)
    image_file = db.Column(db.String(20),default = 'default.jpg', nullable = False)
    result_file = db.Column(db.String(20),default = 'default.jpg', nullable = False)
    course=db.Column(db.String(10),nullable = False)
    email = db.Column(db.String(120), nullable = False)
    password = db.Column(db.String(60),nullable = False)

    marks = db.relationship('Sem1',backref='student',uselist=False)


    def __repl__(self):
        return f"Students({self.id}, {self.name}, {self.email},{self.image_file},{self.result_file},{self.cgpa})"


   
class Admin(db.Model,UserMixin):
    s_no = db.Column(db.Integer(),primary_key = True)
    id = db.Column(db.String(8),unique =True,nullable = False)
    name = db.Column(db.String(25), nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(60),nullable = False)

    def __repl__(self):
        return f"Admin({self.id}, {self.name},{self.email})"
    

class Sem1(db.Model):
    id = db.Column(db.Integer(),primary_key = True)

    student_id = db.Column(db.Integer,db.ForeignKey('student.s_no'),unique = True)
    
    ext_1001 = db.Column(db.Integer(),nullable=False)
    ext_1002 = db.Column(db.Integer(),nullable=False)
    ext_1003 = db.Column(db.Integer(),nullable=False)
    ext_1004 = db.Column(db.Integer(),nullable=False)
    ext_1005 = db.Column(db.Integer(),nullable=False)
    ext_1002P = db.Column(db.Integer(),nullable=False)

    int_1001 = db.Column(db.Integer(),nullable=False)
    int_1002 = db.Column(db.Integer(),nullable=False)
    int_1003 = db.Column(db.Integer(),nullable=False)
    int_1004 = db.Column(db.Integer(),nullable=False)
    int_1005 = db.Column(db.Integer(),nullable=False)
    int_1002P = db.Column(db.Integer(),nullable=False)

    sgpa=db.Column(db.Numeric(precision=8, asdecimal=False, decimal_return_scale=None), default = 0.0)


    def __repl__(self):
        return  f"Sem1({self.id},{self.ext_1001}, {self.ext_1002},{self.ext_1003},{self.ext_1004},{self.ext_1005},{self.ext_1002P},{self.int_1001},{self.int_1002},{self.int_1003},{self.int_1004},{self.int_1005},{self.int_1002P})"
