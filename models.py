from server import db

class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    code = db.Column(db.String(3), nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(10), nullable=False)
    country = db.Column(db.String(10), nullable=True)
    gender = db.Column(db.String(1), nullable=False)
