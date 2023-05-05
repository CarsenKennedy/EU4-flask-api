from enum import unique
from app import db

class AchievementModel(db.Model):
    __tablename__ = 'achievements'
    
    id = db.Column(db.Integer(), unique = True)
    name = db.Column(db.String(), primary_key=True, unique = True)
    description = db.Column(db.String())
    starting_condition = db.Column(db.String())
    requirements = db.Column(db.String())
    version = db.Column(db.Float())
    dlc = db.Column(db.String(), nullable = True)
    difficulty = db.Column(db.String())
    
    def __init__(self,id,name,description,starting_condition,requirements,version,dlc,difficulty):
        self.id = id
        self.name = name
        self.description = description
        self.starting_condition = starting_condition
        self.requirements = requirements
        self.version = version
        self.dlc = dlc
        self.difficulty = difficulty
    
    def serialized(self):
        return {
            'id':self.id,
            'name': self.name,
            'description': self.description,
            'starting_condition': self.starting_condition,
            'requirements': self.requirements,
            'version':self.version,
            'dlc':self.dlc,
            'difficulty':self.difficulty
        }
