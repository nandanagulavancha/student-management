from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed

class StudentForm(FlaskForm):
    name = StringField('Student Name', validators=[DataRequired()])
    photo = FileField('Student Photo', validators=[DataRequired(), FileAllowed(['jpg', 'png', 'jpeg'])])
    certificate = FileField('Certificate', validators=[DataRequired(), FileAllowed(['pdf', 'docx'])])
    submit = SubmitField('Add Student')
