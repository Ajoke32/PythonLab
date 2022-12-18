from flask import Flask
from .extensions import  db,migrate
from .routes.user.user import user
from .routes.main.main import main
from .routes.album.album import album
from .routes.song.song import song
from .models.album import Albums
from .models.song import Song
from .models.album_m_song import AlbumAndSong
from werkzeug.utils import secure_filename

UPLOAD_FOLDER="..static/img"
ALLOWED_EXTENSIONS={'png','jpeg','jpg'}

def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY'] = 'key that hardly to guess'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pymssql://DESKTOP-2P4SQL3/flpy'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
    app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
    db.init_app(app)
    migrate.init_app(app,db)
    app.register_blueprint(user,url_prefix='/user')
    app.register_blueprint(main,url_prefix='/')
    app.register_blueprint(album,url_prefix='/album')
    app.register_blueprint(song, url_prefix='/song')
    return app

