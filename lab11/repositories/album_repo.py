import datetime
from ..extensions import db
from ..models import album as a
from sqlalchemy import select,update,delete
from flask import session
from werkzeug.utils import secure_filename

class AlbumRepository:
    __formats=('png','jpeg','jpg')
    @classmethod
    def add_album(cls,album:dict,file):
        if cls.get_album_by_name(album['name']):
            return False
        if album['name'] and album['desc']:
            file_ref = cls.__make_file_name(file,album['name'])
            if file_ref:
                db.session.add(a.Albums(albumname=album['name'],description=album['desc'],
                                        img=file_ref,
                                        edit_data=datetime.datetime.now(),
                                        editor_name=session['user']))
                db.session.commit()
                return True

        return False

    @classmethod
    def update_album(cls,data:dict,file,album_id):

        stmt = update(a.Albums).where(a.Albums.id == album_id)
        if data:
            stmt = stmt.values(data) \
                .values(edit_data=datetime.datetime.now(), editor_name=session['user'])

        res = cls.get_album_by_id(album_id)
        if 'albumname' in data and data['albumname'] != res.albumname:
            file_ref = cls.__make_file_name(file, data['albumname'])
        else:
            file_ref = cls.__make_file_name(file, res.albumname)

        if file_ref:
            stmt = stmt.values(img=file_ref)

        if data or file_ref:
            db.session.execute(statement=stmt)
            db.session.commit()
        else:
            return False


        return True



    @staticmethod
    def delete(album_id):
        res=AlbumRepository.get_album_by_id(album_id)
        if res:
            stmt = delete(a.Albums).where(a.Albums.id==album_id)
            db.session.execute(statement=stmt)
            db.session.commit()
            return True

        return False

    @staticmethod
    def get_album_by_name(name:str):
        statement=select(a.Albums).filter_by(albumname=name)
        res = db.session.scalars(statement=statement).first()
        if res:
            return res
        else:
            return False

    @staticmethod
    def get_album_by_id(album_id):
        statement = select(a.Albums).filter_by(id=album_id)
        res = db.session.scalars(statement=statement).first()
        if res:
            return res
        else:
            return False

    @staticmethod
    def get_albums():
        stmt=select(a.Albums)
        res = db.session.scalars(statement=stmt).all()
        return res


    @staticmethod
    def __make_file_name(file,key:str):

        if not file or len(file.filename)>37:
            return False

        if file:
            filename = secure_filename(file.filename)
            file_split = filename.split('.')
            if file_split[1] not in AlbumRepository.__formats:
                return False
            file_ref = F"{file_split[0]}{key[:3]}.{file_split[1]}"
            file.save(F"lab11/static/img/{file_ref}")
        else:
            return False

        return  file_ref