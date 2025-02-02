from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from models import db, Student
from forms import StudentForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
db.init_app(app)

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = StudentForm()
    if form.validate_on_submit():
        photo = form.photo.data
        certificate = form.certificate.data

        photo_filename = secure_filename(photo.filename)
        certificate_filename = secure_filename(certificate.filename)

        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], photo_filename))
        certificate.save(os.path.join(app.config['UPLOAD_FOLDER'], certificate_filename))

        new_student = Student(name=form.name.data, photo=photo_filename, certificate=certificate_filename)
        db.session.add(new_student)
        db.session.commit()
        return redirect(url_for('index'))

    students = Student.query.all()
    return render_template('index.html', form=form, students=students)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
