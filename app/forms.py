from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField ('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField()


class UserInfoForm(FlaskForm):	
    username = StringField('Username', validators=[DataRequired()])	   
    email = StringField('Email', validators=[DataRequired(), Email()])	   
    password = PasswordField('Password', validators=[DataRequired()])	    
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])	
    submit = SubmitField()