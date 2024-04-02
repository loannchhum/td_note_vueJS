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

def supprimer_questionnaire(id_questionnaire):
    """
        Delete a questionnaire
        Args:
            id_questionnaire (int): Id of the questionnaire
        Returns:
            None
    """
    questionnaire = Questionnaire.query.get(id_questionnaire)
    db.session.delete(questionnaire)
    db.session.commit()
    # on supprime les questions associees
    questions = Question.query.filter_by(questionnaire_id=id_questionnaire).all()
    for question in questions:
        db.session.delete(question)
    db.session.commit()
    
    
def modifier_questionnaire(id_questionnaire, name):
    """
        Modify a questionnaire
        Args:
            id_questionnaire (int): Id of the questionnaire
            name (str): Name of the questionnaire
        Returns:
            None
    """
    questionnaire = Questionnaire.query.get(id_questionnaire)
    questionnaire.name = name
    db.session.commit()
    
def get_max_id_questionnaire():
    """
        Get the maximum id of the questionnaire
        Args:
            None
        Returns:
            int: Maximum id of the questionnaire
    """
    return db.session.query(db.func.max(Questionnaire.id)).scalar()
    
    
def cree_questionnaire(name):
    """
        Create a questionnaire
        Args:
            name (str): Name of the questionnaire
        Returns:
            None
    """
    # on verifie si le questionnaire existe deja
    if name != '' and name is not None and Questionnaire.query.filter_by(name=name).first() is None:
        questionnaire = Questionnaire(id=get_max_id_questionnaire()+1,name=name)
        db.session.add(questionnaire)
        db.session.commit()
        return True
    return False

def get_max_id_question():
    """
        Get the maximum id of the question
        Args:
            None
        Returns:
            int: Maximum id of the question
    """
    return db.session.query(db.func.max(Question.id)).scalar()

def cree_question_simple(title, questionnaire_id, choix1, choix2, reponse):
    """
        Create a simple question
        Args:
            title (str): Title of the question
            questionnaire_id (int): Id of the questionnaire
            choix1 (str): First choice
            choix2 (str): Second choice
            reponse (str): Answer
        Returns:
            None
    """
    # on verifie si la question existe deja
    print(Question.query.filter_by(title=title).first())
    if Question.query.filter_by(title=title).first() is None:
        print(questionnaire_id, title, choix1, choix2, reponse)
        question = QuestionSimple(id=get_max_id_question()+1, title=title, question_type='simplequestion', questionnaire_id=questionnaire_id, choix1=choix1, choix2=choix2, reponse=reponse)
        print("zabdhzbhdbez")
        db.session.add(question)
        db.session.commit()
        
def cree_question_multiple(title, questionnaire_id, choix1, choix2, choix3, choix4, reponse):
    """
        Create a multiple question
        Args:
            title (str): Title of the question
            questionnaire_id (int): Id of the questionnaire
            choix1 (str): First choice
            choix2 (str): Second choice
            choix3 (str): Third choice
            choix4 (str): Fourth choice
            reponse (str): Answer
        Returns:
            None
    """
    

    print(questionnaire_id, title, choix1, choix2,choix3,choix4, reponse)
    if Question.query.filter_by(title=title).first() is None:
        question = QuestionMultiple(id=get_max_id_question()+1, title=title, question_type='multiplequestion', questionnaire_id=questionnaire_id, choix1=choix1, choix2=choix2, choix3=choix3, choix4=choix4, reponse=reponse)
        
        db.session.add(question)
        db.session.commit()
    
def mettre_a_jour_question_simple(id_question, title, choix1, choix2, reponse):
    """
        Modify a simple question
        Args:
            id_question (int): Id of the question
            title (str): Title of the question
            choix1 (str): First choice
            choix2 (str): Second choice
            reponse (str): Answer
        Returns:
            None
    """
    question = QuestionSimple.query.get(id_question)
    question.title = title
    question.choix1 = choix1
    question.choix2 = choix2
    question.reponse = reponse
    db.session.commit()

def mettre_a_jour_question_multiple(id_question, title, choix1, choix2, choix3, choix4, reponse):
    """
        Modify a multiple question
        Args:
            id_question (int): Id of the question
            title (str): Title of the question
            choix1 (str): First choice
            choix2 (str): Second choice
            choix3 (str): Third choice
            choix4 (str): Fourth choice
            reponse (str): Answer
        Returns:
            None
    """
    question = QuestionMultiple.query.get(id_question)
    question.title = title
    question.choix1 = choix1
    question.choix2 = choix2
    question.choix3 = choix3
    question.choix4 = choix4
    question.reponse = reponse
    db.session.commit()

def supprimer_question(id_question):
    """
        Delete a question
        Args:
            id_question (int): Id of the question
        Returns:
            None
    """
    print(1)
    question = Question.query.get(id_question)
    print(2)
    db.session.delete(question)
    print(3)
    db.session.commit()
    print(4)