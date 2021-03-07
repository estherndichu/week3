from flask_login import login_required,current_user
from flask import render_template,request,redirect,url_for,abort
from ..models import User,Pitches,Comments
from . import main
from .. import db,photos
from . import main
from .forms import PitchForm,UpdateProfile,CommentForm

@main.route('/')
def index():
    '''
    Index page
    return
    '''
    interview = Pitches.query.filter_by(category = 'Interview').all() 
    promotion = Pitches.query.filter_by(category = 'Promotion').all()
    pickup = Pitches.query.filter_by(category = 'Pickup').all()
    return render_template('index.html', promotion = promotion,interview = interview, pickup=pickup)

@main.route('/pitch/', methods = ['GET','POST'])
@login_required
def new_pitch():

    form = PitchForm()

    if form.validate_on_submit():
        pitch_title=form.pitch_title.data
        category = form.category.data
        pitch= form.pitch.data
        user_id=current_user

        new_pitch = Pitches(pitch_title=pitch_title,category= category,pitch= pitch,user_id=current_user.id)

        title='New Pitch'

        new_pitch.save_pitch()

        return redirect(url_for('main.index'))

    return render_template('pitch.html',form= form)

@main.route('/categories/<category>')
@login_required
def category(category):
    '''
    function to return the pitches by category
    '''
    category = Pitches.get_pitches(category)
    title = f'{category}'
    return render_template('categories.html',title = title, category = category)    

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(author = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)   


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)   

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))    


@main.route('/new_comment/<int:pitch_id>', methods = ['GET', 'POST'])
@login_required
def new_comment(pitch_id):
    pitches = Pitches.query.filter_by(id = pitch_id).first()
    form = CommentForm()

    if form.validate_on_submit():
        comment = form.comment.data
        pitch_id=pitch_id
        user_id=current_user._get_current_object().id

        new_comment = Comments(comment=comment,user_id=current_user.id, pitch_id=pitch_id)

        new_comment.save_comment()

        return redirect(url_for('main.index'))
    title='New comment'
    return render_template('new_comment.html',title=title,comment_form = form,pitch_id=pitch_id)

    