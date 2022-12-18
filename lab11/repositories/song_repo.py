from ..extensions import db
from ..models.song import Song
from sqlalchemy import select
from werkzeug.utils import secure_filename


class SongRepository:

    @staticmethod
    def add_song(song:dict,file):
        file_ref=''
        if SongRepository.get_song_by_name(song['song_name']):
            return False

        if len(file.filename)>37:
            return False

        if file:
            filename = secure_filename(file.filename)
            file_split = filename.split('.')
            file_ref = F"{file_split[0]}{song['song_name'][:3]}.{file_split[1]}"
            if file_split[1]!='mp3':
                return False

        if song and song['song_name']:
            db.session.add(Song(song_name=song['song_name'],audio=file_ref,link=song['link']))
            db.session.commit()
            if file:
                file.save(F"lab11/static/audio/{file_ref}")
            return True

        return False


    @staticmethod
    def get_song_by_name(name):
        stmt=select(Song).filter_by(song_name=name)
        res = db.session.scalars(statement=stmt).first()
        if res:
            return res
        else:
            return False


