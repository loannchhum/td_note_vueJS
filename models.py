# models.py
from flask_sqlalchemy import SQLAlchemy
from .app import db

Base = db.Model
metadata = Base.metadata

class Questionnaire(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), index=True, unique=True)

    def __repr__(self):
        return '<Questionnaire (%d) %r>' % (self.id, self.name)
    
    def __init__(self,id, name):
        self.id = id
        self.name = name
        
    def to_json(self):
        json={
            'id': self.id,
            'name': self.name,
        }
        return json

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(120))  # Changed from 'question' to 'title'
    question_type = db.Column(db.String(120))
    questionnaire_id = db.Column(db.Integer, db.ForeignKey('questionnaire.id'))
    questionnaire = db.relationship('Questionnaire',
        backref=db.backref('questions', lazy='dynamic'))
    reponse = db.Column(db.String(120))
    
    def __repr__(self):
        return '<Question (%d) %r>' % (self.id, self.title)  # Changed from 'question' to 'title'


    __mapper_args__ = {
        'polymorphic_identity':'question',
        'polymorphic_on':question_type,
    }

    def __init__(self,id, title, question_type, questionnaire_id,reponse):
        self.id = id
        self.title = title
        self.question_type = question_type
        self.questionnaire_id = questionnaire_id
        self.reponse=reponse
        
    def to_json(self):
        json={
            'id': self.id,
            'title': self.title,  # Changed from 'question' to 'title'
            'questionnaire_id': self.questionnaire_id,
            'reponse': self.reponse,
        }
        return json


class QuestionSimple(Question):
    id = db.Column(db.Integer, db.ForeignKey('question.id'), primary_key=True)
    choix1 = db.Column(db.String(120))
    choix2 = db.Column(db.String(120))

    def __repr__(self):
        return '<QuestionSimple (%d) %r>' % (self.id, self.choix1)
    
    __mapper_args__ = {
        'polymorphic_identity':'simplequestion',
        'with_polymorphic':'*',
        'polymorphic_load':'inline'
    }
    def __init__(self,id, title, question_type,questionnaire_id, choix1, choix2, reponse):
        super().__init__(id,title, question_type, questionnaire_id,reponse)  # Initialize base class
        self.choix1 = choix1
        self.choix2 = choix2

    def to_json(self):
        json = super().to_json() 
        json.update({
            'choix1': self.choix1,
            'choix2': self.choix2,
        })
        return json
    
class QuestionMultiple(Question):
    id = db.Column(db.Integer, db.ForeignKey('question.id'), primary_key=True)
    choix1 = db.Column(db.String(120))
    choix2 = db.Column(db.String(120))
    choix3 = db.Column(db.String(120))
    choix4 = db.Column(db.String(120))

    def __repr__(self):
        return '<QuestionMultiple (%d) %r>' % (self.id, self.choix1)
    
    __mapper_args__ = {
        'polymorphic_identity':'multiplequestion',
        'with_polymorphic':'*',
        'polymorphic_load':'inline'
    }
    
    def __init__(self,id, title, question_type,questionnaire_id, choix1, choix2, choix3, choix4, reponse):
        super().__init__(id,title, question_type, questionnaire_id,reponse)  # Initialize base class
        self.choix1 = choix1
        self.choix2 = choix2
        self.choix3 = choix3
        self.choix4 = choix4

    def to_json(self):
        json = super().to_json() 
        json.update({
            'choix1': self.choix1,
            'choix2': self.choix2,
            'choix3': self.choix3,
            'choix4': self.choix4,
        })
        return json


def get_all_questionnaires():
    """
        Get all questionnaires
        Args:
            None
        Returns:
            list: List of all questionnaires
    
    """
    return Questionnaire.query.all()

def get_question_by_questionnaire_id(questionnaire_id):
    """
        Get all questions for a questionnaire
        Args:
            questionnaire_id (int): Id of the questionnaire
        Returns: 
            list: List of all questions for the questionnaire
    """
    return Question.query.filter_by(questionnaire_id=questionnaire_id).all()