from flask.blueprints import Blueprint
from flask import make_response,request,render_template
from ...repositories import song_repo as s

repo = s.SongRepository()

song = Blueprint('song',__name__,template_folder='templates',static_folder='static')


@song.route('/add',methods=['POST'])
def add_song():
    if request.method=='POST':
        res=repo.add_song(request.form,request.files['audio'])
        if res:
            return make_response({'add':'success','msg':'Song added'})

    return make_response({'add':'fail','msg':'Song already exist!'})


