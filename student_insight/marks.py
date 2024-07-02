from student_insight import db
from student_insight.models import Student

class Sem1(db.Model):
    id = db.Column(db.Integer(),primary_key = True)

    student_id = db.Column(db.Integer,db.ForeignKey('Student.s_no'),unique = True)
    
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