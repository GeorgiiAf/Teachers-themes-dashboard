from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.fields.choices import SelectField
from wtforms.fields.simple import BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError

from .models.user import User


class RegistrationForm(FlaskForm):
    name = StringField(
        'Full name',
        validators=[DataRequired(), Length(min=2, max=50)],
        render_kw={'class': 'form-control', 'placeholder': 'Full name'}
    )

    login = StringField(
        'Login',
        validators=[DataRequired(), Length(min=2, max=50)],
        render_kw={'class': 'form-control', 'placeholder': 'Login'}
    )

    password = PasswordField(
        'Password',
        validators=[DataRequired()],
        render_kw={'class': 'form-control', 'placeholder': 'Password'}
    )

    confirm_password = PasswordField(
        'Confirm Password',
        validators=[DataRequired(), EqualTo('password')],
        render_kw={'class': 'form-control', 'placeholder': 'Confirm password'}
    )

    avatar = FileField(
        'Upload your avatar',
        validators=[FileAllowed(['jpg', 'jpeg', 'png'])],
        render_kw={'class': 'form-control'}
    )

    submit = SubmitField(
        'Sign in',
        render_kw={'class': 'btn btn-success'}
    )



    def validate_login(self , login):
        user = User.query.filter_by(login = login.data).first()
        if user:
            raise ValidationError('This login is already exists...')



class LoginForm(FlaskForm):
    """FORM to log in users"""

    login = StringField(
        'Login',
        validators=[DataRequired(), Length(min=2, max=50)],
        render_kw={'class': 'form-control', 'placeholder': 'Login'}
    )

    password = PasswordField(
        'Password',
        validators=[DataRequired()],
        render_kw={'class': 'form-control', 'placeholder': 'Password'}
    )

    remember = BooleanField('Remember me')


    submit = SubmitField(
        'Login',
        render_kw={'class': 'btn btn-success'}
    )



class StudentForm(FlaskForm):
    student = SelectField('student', choices=[], render_kw={'class': 'form-control'})


class TeacherForm(FlaskForm):
    teacher = SelectField('reacher', choices=[], render_kw={'class': 'form-control'})


