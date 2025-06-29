from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Calculation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    voltage = db.Column(db.Float)
    current = db.Column(db.Float)
    pf = db.Column(db.Float)
    phase = db.Column(db.String(10))
    real_power = db.Column(db.Float)
    reactive_power = db.Column(db.Float)
    apparent_power = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))