from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,SelectField,TextAreaField
from wtforms.validators import Required
from ..models import User

class PitchForm(FlaskForm):
    pitch_title = StringField('Pitch Title')
    category = SelectField (u'Pitch Categories', choices = [('Pickup','Pickup'),('Interview','Interview'),('Promotion','Promotion')])
    pitch = TextAreaField('Pitch')
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Comment Below')
    submit = SubmitField('Comment')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about yourself',validators =[Required()])  
    submit = SubmitField('Submit')      