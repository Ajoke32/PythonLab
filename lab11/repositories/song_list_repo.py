from ..models import album_m_song as m
from ..models import song as s
from ..extensions import db
from sqlalchemy import select


class SongList:

    @staticmethod
    def add_song_and_album(song_id:int,album_id:int):
        if song_id and album_id:
            db.session.add(m.AlbumAndSong(song_id=song_id,album_id=album_id))
            db.session.commit()
            return True

        return False

    @staticmethod
    def get_album_song_list(album_id:int):
        stmt = select(m.AlbumAndSong.id,s.Song.song_name,s.Song.audio)\
            .filter(m.AlbumAndSong.song_id==s.Song.id)\
            .filter_by(album_id=album_id).join(s.Song)

        res = db.session.execute(stmt).all()
        if res:
            return res
        else:
            return False