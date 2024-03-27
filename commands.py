from .models import  db, Questionnaire, QuestionSimple, QuestionMultiple
from .app import app

@app.cli.command('initDB')
def initDB():
    db.drop_all()
    db.create_all()
    print('Base de donnees initialisee.')
    


    # Creer une session pour interagir avec la base de donnees
    questionnaires = [
        Questionnaire(1,name='Maths'),
        Questionnaire(2,name='Histoire'),
        Questionnaire(3,name='Web'),]
    db.session.add_all(questionnaires)

    questions = [
        QuestionSimple(1,title='Quel est le resultat de 2+2 ?', question_type='simplequestion', questionnaire_id=1,choix1="4",choix2="5",reponse="4"),
        QuestionSimple(2,title='Quel est le resultat de 3+3 ?', question_type='simplequestion', questionnaire_id=1,choix1="6",choix2="7",reponse="6"),
        QuestionMultiple(3,title='anne de la revolution ?', question_type='multiplequestion', questionnaire_id=2,choix1="1788",choix2="1789",choix3="1787",choix4="1790",reponse="1789"),
        ]
    db.session.add_all(questions)


    db.session.commit()
