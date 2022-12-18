from ..extensions import db


class Song(db.Model):
    ___tablename__ = 'songs'
    id = db.Column(db.Integer, primary_key=True)
    song_name = db.Column(db.String(40), nullable=False)
    link = db.Column(db.String(150),nullable=True)
    audio = db.Column(db.String(40),nullable=True)

    def __repr__(self):
        return F"{self.id}"
