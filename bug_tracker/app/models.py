from app import db
from datetime import datetime

class Bug(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    bug_type = db.Column(db.String(50), nullable=False)
    bug_description = db.Column(db.String(1000), nullable=False)
    bug_priority = db.Column(db.String(30), nullable=False)
    bug_status = db.Column(db.String(30), default='Not Assigned Yet')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Bug {self.id} - {self.bug_type}>'
