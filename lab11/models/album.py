from ..extensions import db

class Albums(db.Model):
    ___tablename__='albums'
    id=db.Column(db.Integer,primary_key=True)
    albumname=db.Column(db.String(40),nullable=False)
    description=db.Column(db.String('max'),nullable=False)
    img = db.Column(db.String(40), nullable=False)
    edit_data=db.Column(db.DateTime,nullable=False)
    editor_name = db.Column(db.String(25),nullable=False)

    def __repr__(self):
        return F"{self.albumname,self.description,self.img,self.edit_data,self.editor_name}"



