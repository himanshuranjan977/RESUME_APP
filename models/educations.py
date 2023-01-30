from config import db

class Educations(db.Model):
    __tablename__ = 'educations'
    id = db.Column(db.Integer, primary_key=True)
    school_name = db.Column(db.String(200), nullable=False)
    degree_name = db.Column(db.String(200), nullable=False)
    start_date = db.Column(db.String(200), nullable=False)
    end_date = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))