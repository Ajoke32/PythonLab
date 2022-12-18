from flask import Blueprint,request,flash,session,redirect,url_for

from flask import render_template
from ...repositories.user_repo import UserRepository


user = Blueprint('user',__name__,template_folder='templates',static_folder='static')
repo = UserRepository()


@user.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        if not repo.login(request.form):
            flash('Make sure that passwod and login are correct',category='fail')
        else:
            return redirect(url_for('main.main_page'))

    return render_template('user/login.html', session=session)

@user.route('/logout')
def logout():
    repo.logout()
    return redirect(url_for('main.main_page'))

@user.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        repo.add_user(request.form)

    return render_template('user/register.html')
