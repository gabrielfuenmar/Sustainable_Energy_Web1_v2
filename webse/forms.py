from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, InputRequired
from webse.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    course = SelectField('Course', validators=[DataRequired()],
                             choices=[('ENE425 Sustainable Energy and App Development', 'ENE425 Sustainable Energy and App Development'),
                                      ('Guest Course', 'Guest Course')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')

class ChatForm(FlaskForm):
    chat_module = SelectField('Select a chat module:', validators=[DataRequired()],
                       choices=[('Home Chat', 'Home Chat'),
                                ('App Module Chat', 'App Module Chat'),
                                ('Sustainable Energy Module Chat', 'Sustainable Energy Module Chat'),
                                ('Informal Chat', 'Informal Chat')])
    chat_group = SelectField('Select a chat group:', validators=[DataRequired()],
                              choices=[('All', 'All'),
                                       ('Group 1', 'Group 1'),
                                       ('Group 2', 'Group 2'),
                                       ('Group 3', 'Group 3')])
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Chat')

class ChatQueryForm(FlaskForm):
    chat_module = SelectField('Select a chat module:', validators=[DataRequired()],
                       choices=[('Home Chat', 'Home Chat'),
                                ('App Module Chat', 'App Module Chat'),
                                ('Sustainable Energy Module Chat', 'Sustainable Energy Module Chat'),
                                ('Informal Chat', 'Informal Chat')])
    chat_group = SelectField('Select a chat group:', validators=[DataRequired()],
                              choices=[('All', 'All'),
                                       ('Group 1', 'Group 1'),
                                       ('Group 2', 'Group 2'),
                                       ('Group 3', 'Group 3')])
    submit = SubmitField('Chat Query')

class ChatFormUpdate(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Chat')

class ChatFormExercise(FlaskForm):
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Chat')

class AnnouncementForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Annoucement')

class QuestionFormExercise(FlaskForm):
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Question')

#App Statistics
#App Statistics
class ModStatisticsForm(FlaskForm):
    mod_type = SelectField(validators=[InputRequired()],
                        choices=[('App Development', 'App Development'),
                                 ('Sustainable Energy', 'Sustainable Energy')])
    chapter = SelectField("Chapter",
                         validators=[InputRequired()],choices=[])
    
    submit = SubmitField('Submit')

#M1_Ch1
class ModulsForm_M1_Ch1_Q1(FlaskForm):
    type = SelectField(validators=[DataRequired()],
                       choices=[('Python', 'Python'),
                                ('HTML', 'HTML')])
    submit = SubmitField('Programming Language')

class ModulsForm_M1_Ch1_Q2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('GitHub', 'GitHub'),
                                ('Heroku', 'Heroku')])
    submit = SubmitField('Server')

class ModulsForm_M1_Ch1_Q3(FlaskForm):
    type = RadioField(choices=['Easy', 'Medium', 'Difficult'],
                       validators=[InputRequired()])
    submit = SubmitField('Implementation')

#M1_Ch2
class ModulsForm_M1_Ch2_Q1(FlaskForm):
    identifier = StringField()
    question_str = StringField('App Module, Chapter 2, Question 1', validators=[DataRequired()])
    submit1 = SubmitField('Check')

class ModulsForm_M1_Ch2_Q2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('wind', 'wind'),
                                ('solar', 'solar')])
    submit = SubmitField('Type Energy')

class ModulsForm_M1_Ch2_Q3(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                                choices=[('income', 'income'),
                                        ('expense', 'expense')])
    submit = SubmitField('Type Income')

class ModulsForm_M1_Ch2_Q4(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                                choices=[('university', 'university'),
                                        ('school', 'school')])
    submit = SubmitField('Type Work')

class ModulsForm_M1_Ch2_Q5(FlaskForm):
    type = RadioField('Level',
                       choices=['Petrol', 'Electric', 'Hydrogen'],
                       validators=[InputRequired()])
    submit = SubmitField('Type type')

#M2_Ch1: SE, Frame.
class ModulsForm_M2_Ch1_E1(FlaskForm):
    type = SelectField(validators=[DataRequired()],
                       choices=[('Should include only environmental pollution, carbon emissions', 'Should include only environmental pollution, carbon emissions'),
                                ('Should include only poverty alleviation, gender equality', 'Should include only poverty alleviation, gender equality'),
                                ('Should include both', 'Should include both')])
    submit = SubmitField('Submit')

class ModulsForm_M2_Ch1_E2(FlaskForm):
    type = SelectField(validators=[DataRequired()],
                       choices=[('Green Economy is more related to welfare and environmental economics', 'Green Economy is more related to welfare and environmental economics'),
                                ('Green Economy is more related to ecological economics', 'Green Economy is more related to ecological economics'),
                                ('Green Economy is more related to economics schools', 'Green Economy is more related to economics schools')])
    submit = SubmitField('Submit')

class ModulsForm_M2_Ch1_Q1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Should only consider carbon emissions', 'Should only consider carbon emissions'),
                                ('Should only consider electrification', 'Should only consider electrification'),
                                ('Should also consider social aspects', 'Should also consider social aspects')])
    submit = SubmitField('Submit')

class ModulsForm_M2_Ch1_Q2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Pollution is a negative externality', 'Pollution is a negative externality'),
                                ('Sustainability and economy are a subsystem of the ecosystem', 'Sustainability and economy are a subsystem of the ecosystem'),
                                ('Research and technology are fundamental parts of agriculture development', 'Research and technology are fundamental parts of agriculture development')])
    submit = SubmitField('Submit')

#M2_Ch2: SE. Footprint and biocapacity
class ModulsForm_M2_Ch2_E1(FlaskForm):
    type = SelectField(validators=[DataRequired()],
                       choices=[('The ecological footprint should be charged to Norway', 'The ecological footprint should be charged to Norway'),
                                ('The ecological footprint should be charged to Spain', 'The ecological footprint should be charged to Spain'),
                                ('The ecological footprint should be charged partially to both countries', 'The ecological footprint should be charged partially to both countries')])
    submit = SubmitField('Submit')


class ModulsForm_M2_Ch2_Q1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Biologically productive area it takes to satisfy the exporting demand', 'Biologically productive area it takes to satisfy the exporting demand'),
                                ('Biologically productive area it takes to satisfy the demands of people', 'Biologically productive area it takes to satisfy the demands of people'),
                                ('Biologically productive area it takes to satisfy the importing demand', 'Biologically productive area it takes to satisfy the importing demand')])
    submit = SubmitField('Submit')

class ModulsForm_M2_Ch2_Q2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Land and sea area available to provide the resources a population consumes and to absorb its wastes',
                                 'Biologically productive area it takes to satisfy the exporting demand'),
                                ('Biologically productive area it takes to satisfy the demands of people',
                                 'Biologically productive area it takes to satisfy the demands of people'),
                                ('Biologically productive area it takes to satisfy the importing demand',
                                 'Biologically productive area it takes to satisfy the importing demand')])
    submit = SubmitField('Submit')

class ModulsForm_M2_Ch2_Q3(FlaskForm):
    type = RadioField(choices=['Easy', 'Medium', 'Difficult'],
                       validators=[InputRequired()])
    submit = SubmitField('Implementation')