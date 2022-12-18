from ..extensions import db

class Users(db.Model):
    ___tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(25),nullable=True)
    surname=db.Column(db.String(25),nullable=True)
    email=db.Column(db.String(35),nullable=False)
    login=db.Column(db.String(20),nullable=False)
    password_hash=db.Column(db.String(128),nullable=False)

    def __repr__(self):
        return F"{self.login,self.password_hash}"




