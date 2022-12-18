from flask import Blueprint,request,flash,session,redirect,url_for
from flask import render_template
from ...repositories.album_repo import AlbumRepository

main= Blueprint('main',__name__,template_folder='templates',static_folder='static')
repo = AlbumRepository()

@main.route('/')
def main_page():
    albums=repo.get_albums()
    return render_template('main/main.html',al_list=albums)

@main.route('/about_group')
def group_info():
    return render_template('main/group_history.html')

@main.route('/about_prg')
def project_info():
    return render_template('main/abount_prog.html')


