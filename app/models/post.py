from ..extensions import db
from datetime import datetime

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    subject = db.Column(db.String(250))
    discipline = db.Column(db.String(100))
    comment = db.Column(db.Text)
    group_number = db.Column(db.String(20))
    is_checked = db.Column(db.Boolean)
    teacher = db.Column(db.Integer, db.ForeignKey('user.id' , ondelete='CASCADE'))
    student = db.Column(db.Integer)
    date = db.Column(db.DateTime, default=datetime.utcnow)

