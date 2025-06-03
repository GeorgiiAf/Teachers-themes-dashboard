from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.fields.choices import SelectField
from wtforms.fields.simple import BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from wtforms import DateField, TextAreaField
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
        validators=[DataRequired(), Length(min=8, message='Password must be at least 8 characters')],
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

    def validate_login(self, login):
        user = User.query.filter_by(login=login.data).first()
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
    student = SelectField(
        'Student',
        choices=[],
        render_kw={'class': 'form-control'},
        validators=[DataRequired()]
    )
    subject = StringField(
        'Subject',
        validators=[DataRequired(), Length(max=250)],
        render_kw={'class': 'form-control', 'placeholder': 'Enter subject'}
    )
    discipline = StringField(
        'Discipline',
        validators=[DataRequired(), Length(max=100)],
        render_kw={'class': 'form-control', 'placeholder': 'Enter discipline'}
    )
    comment = TextAreaField(
        'Comments',
        validators=[Length(max=500)],
        render_kw={'class': 'form-control', 'placeholder': 'Enter comment', 'rows': 3}
    )
    group_number = StringField(
        'Group Number',
        validators=[ Length(max=20)],
        render_kw={'class': 'form-control', 'placeholder': 'Enter group number'}
    )
    is_checked = BooleanField(
        'Is Checked',
        render_kw={'class': 'form-check-input'}
    )
    deadline = DateField(
        'Deadline',
        format='%Y-%m-%d',
        render_kw={'class': 'form-control'},
        validators=[]
    )


class TeacherForm(FlaskForm):
    teacher = SelectField(
        'Teacher',
        choices=[],
        render_kw={'class': 'form-control'}
    )
    discipline_filter = SelectField(
        'Filter by Discipline',
        choices=[],
        render_kw={'class': 'form-control'}
    )
    group_filter = SelectField(
        'Filter by Group',
        choices=[],
        render_kw={'class': 'form-control'}
    )
    show_checked = BooleanField(
        'Show only checked',
        render_kw={'class': 'form-check-input'}
    )
