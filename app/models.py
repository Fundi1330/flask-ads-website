from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Ads(db.Model):
    __tablename__ = 'Ads'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, index = True, unique = True)
    description = db.Column(db.String, index = True, unique = True)
    
    def __repr__(self) -> str:
        return f'<Ads {self.name}'