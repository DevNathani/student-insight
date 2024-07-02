from flask_mail import Message
from PIL import Image
from werkzeug.utils import secure_filename
from random import randint
from secrets import token_hex
from student_insight.models import Admin,Student,Sem1
from student_insight import app,bcrypt,db,mail
from flask_login import current_user,login_user
import os

def login_procedure(data):
    status = None
    id = data['userid']
    pwd = data['password']
    # try:
    if 'ADM' == id[0:3]:
        user = Admin.query.filter_by(id = id).first()
        if user:
            password = bcrypt.check_password_hash(user.password,pwd)
            if password:
                if login_user(user,remember = False):

                    status = 1

    else:
        student = Student.query.filter_by(id = id).first()
        if student:
            password = bcrypt.check_password_hash(student.password,pwd)
            print(password)
            # status = 6
            if password:
                if login_user(student,remember = False):
                    status = 2
    # except:
        # status = 4 
    # finally:     
            # status = 4
    return status


def generate_student_id(name,course):
    name = name.upper()
    ran = randint(10000,99999)
    space = name.find(" ")
    id = course + name[0] + name[space+1] + str(ran)
    id = id.upper()
    pwd = str(token_hex(8)).upper()
    return (id,pwd)

def student_entry(data,file):
    status=None
    credentials = generate_student_id(data['name'],data['course'])
    
    while Student.query.filter_by(id = credentials[0]).first():
        credentials = generate_student_id(data['name'],data['course'])
     
    hashed_pwd = bcrypt.generate_password_hash(credentials[1]).decode('utf-8')
    image_name = save_image(file)
    if image_name:
        student = Student(id = credentials[0] ,
                        name = data['name'] ,
                        dob = data['dob'] ,
                        fname = data['fname'] ,
                        mob = data['mob'] ,
                        fmob = data['fmob'] ,
                        image_file = image_name,
                        email = data['email'] ,
                        course = data['course'] ,
                        password = hashed_pwd)
    try:
        with app.app_context():
            db.session.add(student)
            db.session.commit()
            status = [1,(credentials[0],data['email'],credentials[1])]
        
    except:
        status = 0
    finally:
        return status
    

def save_image(file):
    if file:
        filename = secure_filename(file.filename)
        pic_fname = token_hex(8)
        _ , _ext = os.path.splitext(filename)
        image = pic_fname + _ext
        image_path = os.path.join(app.root_path,'static/profile_pics/',image)
        # file.save(image_path)

        output_size = (250,250)
        i = Image.open(file)
        i.thumbnail(output_size)
        i.save(image_path)
        return image
    else:
        return None


def send_mail(student):
    with app.app_context():
            msg = Message('Student Entry Confirmation', sender = 'noreply@demo.com', recipients = [current_user.email])
            msg.body = f'''The student has been successfully registered in the Database with
                USERID : {student[1][0]}
                Password : {student[1][2]}
        '''
            mail.send(msg)

            msg2 = Message('Successful Registration', sender = 'noreply@demo.com', recipients = [student[1][1]])
            msg2.body = f'''Your are Successfully Registered with us with
                USERID : {student[1][0]}
                Password : {student[1][2]}

        Thank you for choosing our University
        '''
            mail.send(msg2)
   

def contact_mail(data):
    with app.app_context():
            msg = Message("Query / Feedback Recieved", sender = 'noreply@demo.com', recipients = ['nathanidev2@gmail.com'])
            msg.body = f'''The Customer has sent a Query / Feedback, Here are it Details  
                USERNAME : {data['name']}
                EMAIL : {data['email']}
                SUBJECT : {data['subject']}
                MESSAGE :
                {data['message']}

        '''
            mail.send(msg)

            msg2 = Message("Confirmation of Query Registered", sender = 'noreply@demo.com', recipients = [data['email']])
            msg2.body = f'''Your Query / Feedback has been registered successfully, 
                We will revert back to you ASAP 

        '''
            mail.send(msg2)
 
    return True


def save_result(file):
    if file:
        filename = secure_filename(file.filename)
        fname = token_hex(8)
        _ , _ext = os.path.splitext(filename)
        result = fname + _ext
        file_path = os.path.join(app.root_path,'static/Results/',result)
        file.save(file_path)
        return result
    else:
        return None

def marks_entry(data,file):
    state = None
    id = current_user.s_no
    result = save_result(file)
    if result:
        mark = Sem1(student_id = id,
                    ext_1001 = data['E1001'],
                    ext_1002 = data['E1002'],
                    ext_1003 = data['E1003'],
                    ext_1004 = data['E1004'],
                    ext_1005 = data['E1005'],
                    ext_1002P = data['E1002P'],
                    int_1001 = data['I1001'],
                    int_1002 = data['I1002'],
                    int_1003 = data['I1003'],
                    int_1004 = data['I1004'],
                    int_1005 = data['I1005'],
                    int_1002P = data['I1002P'],
                    sgpa = data['SGPA'])
        
        
    try:
        with app.app_context():
            current_user.cgpa = data['CGPA']
            current_user.result_file = result
            db.session.add(mark)
            db.session.commit()
            state = 1
    except:
        state = None
    finally:
        return state