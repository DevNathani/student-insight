from student_insight import app
from flask import render_template,request,redirect,url_for,flash
from student_insight.utils import login_procedure, send_mail, student_entry,contact_mail,marks_entry
import os
from flask_login import logout_user,current_user,login_required
from student_insight.models import Sem1


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login", methods = ['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    message = None
    if request.method == 'POST':
        data = request.form.to_dict()
        status = login_procedure(data)
        if status == 1:
            flash("You are Successfully Logged In")
            
            return redirect(url_for('admin'))
        elif status == 2:
            flash("You are Successfully Logged In")
            return redirect(url_for('home'))
        elif status == 4:
            message = "Something Went Wrong"
        else:
            message = "Invalid Credentials"
            
    return render_template("login.html",message = message)

@app.route('/admin', methods = ['POST','GET'])
@login_required
def admin():
    state1 = None
    state2 = None
    state3 = None
    if request.method == 'POST':
        data = request.form.to_dict()
        file = request.files['profile']
        _ , f_ext = os.path.splitext(file.filename)
        # print(file.filename,_,f_ext)
        if data['course'] != 'Choose...':
            if f_ext in ['.png','.jpg']:
                state3 = student_entry(data,file)
                if state3:
                    flash("Student Registered Successfully", category='success')
                    send_mail(state3)
                    return redirect(url_for('admin'))
                else:
                    flash("Something Went Wrong", category='danger')
                    
                    return redirect(url_for('admin'))

            else:
                state1 = "Invalid File Format"
        else:
            state2 = "Choose the Course"
    return render_template("AdminForm2.html",message = [state1,state2])
    

@app.route("/upload", methods = ['Get','POST'])
@login_required
def upload_marks():
    state1 = state2 = None
    user = None
    id = current_user.s_no
    if Sem1.query.filter_by(student_id = id).first():
        user = 1
    if request.method == 'POST':
        data = request.form.to_dict()
        file = request.files['result']
        _ , f_ext = os.path.splitext(file.filename)
        if f_ext == '.pdf':
            state1 = marks_entry(data,file)
            if state1:
                flash("Marks Have Been Uploaded Successfully", category='success')
                return redirect(url_for('upload_marks'))
            else:
                flash("Something Went Wrong", category='danger')
        else:
            state2 = "Invalid File Format"

    return render_template("upload_marks.html", errors=state2, check_user = user)

@app.route("/contact-us" ,methods = ['POST','GET'])
def contact():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        state = contact_mail(data)
        if state:
            flash('Thankyou for Contacting Us')
            return redirect(url_for('contact'))
    return render_template("contact-us.html")


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))
