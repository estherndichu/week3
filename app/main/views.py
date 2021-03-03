from flask_login import login_required,current_user
from flask import render_template,request,redirect,url_for,abort
from ..models import User,Pitches,Comments
from . import main
from .. import db
from . import main
from .forms import PitchForm,CommentForm,UpdateProfile

@main.route('/')
def index():
    '''
    Index page
    return
    '''
    message= "Welcome to Pitch Application"
    title= 'PITCH APP'
    return render_template('index.html', message=message,title=title)

@main.route('/pitch/', methods = ['GET','POST'])
@login_required
def new_pitch():

    form = PitchForm()

    if form.validate_on_submit():
        category = form.category.data
        pitch= form.pitch.data
        title=form.title.data

        new_pitch = Pitches(title=title,category= category,pitch= pitch,user_id=current_user.id)

        title='New Pitch'

        new_pitch.save_pitch()

        return redirect(url_for('main.index'))

    return render_template('pitch.html',form= form)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(author = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)    