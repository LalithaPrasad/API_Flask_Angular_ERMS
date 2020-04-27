import os
from app_package import db
from datetime import datetime,timedelta
from werkzeug.security import generate_password_hash, check_password_hash

class Admin(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(64))
    password_hash=db.Column(db.String(128))
    token=db.Column(db.String(128))
    token_expiry=db.Column(db.DateTime)

    def set_password(self,password):
        self.password_hash=generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    def get_token(self):
        self.token=os.urandom(3).hex()
        self.token_expiry=datetime.utcnow()+timedelta(seconds=360)
        return self.token

    def validate_token(self):
        return (datetime.utcnow()+timedelta(seconds=60))<self.token_expiry

    def invalidate_token(self):
        self.token_expiry=datetime.utcnow()-timedelta(seconds=60)

class Employee(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(64))
    age=db.Column(db.Integer)
    ed=db.Column(db.String(64))
    role=db.Column(db.String(64))
