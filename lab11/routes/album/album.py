import os.path
from pathlib import Path
from flask import Blueprint,request,flash,session,redirect,url_for,render_template,make_response,jsonify
from werkzeug.utils import secure_filename
from ...repositories.album_repo import AlbumRepository
from ...repositories.song_repo import SongRepository
from ...repositories.song_list_repo import SongList
album= Blueprint('album',__name__,template_folder='templates',static_folder='static')
repo = AlbumRepository()
song_repo = SongRepository()
song_list=SongList()



@album.route('/add',methods=['POST','GET'])
def add_album():
    if request.method=='POST' and request.files:
        res = repo.add_album(request.form,request.files['pict'])
        if res:
            return make_response({'add':'success','msg':'Album added, check main page!'},200)
        else:
            return make_response({'add':'fail','msg':'Make sure the fields are correct and album is new!'},422)
    elif request.method!='GET':
        return make_response({'add': 'fail', 'msg': 'Make sure the fields are correct and album is new!'}, 422)

    return render_template('add_album.html')

@album.route('/update/<album_id>',methods=['POST','GET'])
def update_aldum(album_id):
    if request.method=='POST':
        file=None
        if request.files:
            file=request.files['img']
        res = repo.update_album(request.form,file,album_id)
        if res:
            return make_response({'add':'success','msg':'update was successful, refresh page'})
    return make_response({'add':'not ok'})

@album.route('/entities/add',methods=['POST'])
def add_entites():
    if request.method=='POST':
        if 'id' in request.form and request.form['song_name']:
            song_entity = song_repo.get_song_by_name(request.form['song_name'])
            res = song_list.add_song_and_album(song_entity.id, int(request.form['album_id']))
            if res:
                return make_response({'add':'success','msg':'successfully'},200)

        album_entity = repo.get_album_by_name(request.form['album_name'])
        song_entity = song_repo.get_song_by_name(request.form['song_name'])
        if not album_entity or not song_entity:
            return make_response({'add':'fail','msg':'song or album not exist'},422)
        song_list.add_song_and_album(song_entity.id,album_entity.id)

    return make_response({'add':'success','msg':'successfully'},200)

@album.route('/delete/<album_id>',methods=['POST'])
def delete_alum(album_id):
    res = repo.delete(album_id)
    if res:
        return render_template('main/main.html')

    return make_response({'del':'success','msg':'deleted'})

@album.route('/<album_id>',methods=['GET'])
def album_page(album_id):
    album_entity=repo.get_album_by_id(album_id)
    songs = song_list.get_album_song_list(album_id)
    return render_template('album_page.html',album_entity=album_entity,songs=songs)


