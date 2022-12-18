from ..extensions import db


class AlbumAndSong(db.Model):
    ___tablename__ = 'albums_songs'
    id = db.Column(db.Integer, primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey('song.id'),nullable=False)
    album_id = db.Column(db.Integer, db.ForeignKey('albums.id'),nullable=False)

