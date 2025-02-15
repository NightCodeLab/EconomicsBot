from database import db
from sqlalchemy.sql import func

class Income(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    add = db.Column(db.Integer, nullable=False)
    user = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)
    created_at = db.Column(db.DateTime, default=func.now())

class Spending(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    summ = db.Column(db.Integer, nullable=False)
    user = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)
    created_at = db.Column(db.DateTime, default=func.now())
