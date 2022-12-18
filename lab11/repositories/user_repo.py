from ..extensions import db
from ..models import user_model as u
from sqlalchemy import select
from flask import session,flash
from werkzeug.security import check_password_hash,generate_password_hash

class UserRepository:

    @classmethod
    def add_user(cls,name:dict):
        if cls.get_user_by_login(name['login']):
            return flash('Account already created',category='fail')

        if cls.get_user_by_email(name['email']):
            return flash('Account already created',category='fail')


        if name['email'] and name['login'] and len(name.keys())==5:
            if len(name['password']) <= 5:
                return flash('Password length must be >4',category='fail')
            db.session.add(u.Users(username=name['name'],surname=name['surname']
                                       , email=name['email'],login=name['login'],
                                       password_hash=generate_password_hash(name['password'])))
            db.session.commit()

            return flash('Account created',category='success')

        return flash('Make sure that field not empty',category='fail')

    @staticmethod
    def get_user_by_email(email:str):
        statement = select(u.Users).filter_by(email=email)
        res=db.session.execute(statement=statement).first()
        if res:
            return res
        else:
            return False

    @staticmethod
    def get_user_by_login(login):
        statement = select(u.Users).filter_by(login=login)
        res = db.session.scalars(statement=statement).first()
        if res:
            return res
        else:
            return False

    @classmethod
    def login(cls,data:dict):
        if len(data.keys())!=2:
            return False

        res = cls.get_user_by_login(data['login'])
        if res and check_password_hash(res.password_hash,data['password']):
            session['is_log']=1
            session['user']=res.login
            return True

        return False

    @staticmethod
    def logout():
        session['is_log']=0
