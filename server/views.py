from flask import jsonify, request, abort, make_response, url_for
from .app import app
from .models import *

@app.route('/quiz/api/v1.0/questionnaire', methods=['GET'])
def questionnaire():
    """
        Get all questionnaires
        Args:
            None
        Returns:
            list: List of all questionnaires
    """
    questionnaires = get_all_questionnaires()
    return jsonify({'questionnaires': [questionnaire.to_json() for questionnaire in questionnaires]})



@app.errorhandler(404)
def not_found(error):
    """
        Not found error
    """
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def bad_request(error):
    """
        Bad request error
    """
    return make_response(jsonify({'error': 'Bad request'}), 400)


@app.route('/quiz/api/v1.0/questionnaire/<int:questionnaire_id>', methods=['GET'])
def get_question_questionnaire(questionnaire_id):
    """
        Get all questions for a questionnaire
        Args:
            questionnaire_id (int): Id of the questionnaire
        Returns:
            list: List of all questions for the questionnaire
    """
    questions = get_question_by_questionnaire_id(questionnaire_id)
    print(questions)
    return jsonify({'questions': [question.to_json() for question in questions]})


@app.route('/quiz/api/v1.0/questionnaire/<int:questionnaire_id>', methods=['DELETE'])
def delete_questionnaire(questionnaire_id):
    """
        Delete a questionnaire
        Args:
            questionnaire_id (int): Id of the questionnaire
        Returns:
            None
    """
    supprimer_questionnaire(questionnaire_id)
    return jsonify({'result': True})


@app.route('/quiz/api/v1.0/questionnaire/<int:questionnaire_id>', methods=['PUT'])
def update_questionnaire(questionnaire_id):
    """
        Modify a questionnaire
        Args:
            questionnaire_id (int): Id of the questionnaire
        Returns:
            None
    """
    if not request.json:
        abort(400)
    modifier_questionnaire(questionnaire_id, request.json.get('name', ''))
    db.session.commit()
    return jsonify({'result': True})



@app.route('/quiz/api/v1.0/questionnaire', methods=['POST'])
def create_questionnaire():
    """
        Create a questionnaire
        Args:
            None
        Returns:
            None
    """
    if not request.json or not 'name' in request.json:
        abort(400)
    if cree_questionnaire(request.json.get('name', '')):
        print('bon')
        return jsonify({'result': True}), 201
    return jsonify({'result': False}), 400
    
@app.route('/quiz/api/v1.0/questionnaire/question', methods=['POST'])
def create_question():
    """
        Create a question
        Args:
            None
        Returns:
            None
    """
    print('test'),
    print(request.json.get('title', ''), request.json.get('choix1',''),request.json.get('choix2',''),request.json.get('reponse', ''), request.json.get('questionnaire_id', ''), request.json.get('choix3',''),request.json.get('choix4',''))
    if not request.json:
        print("0000000")
        abort(400)
    # si la longueur de la request est inferieur ou egale 6
    elif request.json.get('title', '') == '' or request.json.get('questionnaire_id', '') == '' or request.json.get('choix1','') == '' or request.json.get('choix2','') == '' or request.json.get('reponse', '') == '':
        print(0)
        return jsonify({'result': False}), 400
    elif len(request.json) < 6:
        # si la fonction cree_question_simple retourne True
        print(1)
        cree_question_simple(request.json.get('title', ''), request.json.get('questionnaire_id', ''), request.json.get('choix1',''),request.json.get('choix2',''),request.json.get('reponse', ''))

        return jsonify({'result': True}), 201
    
    elif len(request.json) > 6:
        print(2)
        
        cree_question_multiple(request.json.get('title', ''), request.json.get('questionnaire_id', ''), request.json.get('choix1',''),request.json.get('choix2',''),request.json.get('choix3',''),request.json.get('choix4',''),request.json.get('reponse', ''))
        return jsonify({'result': True}), 201
    else:
        return jsonify({'result': False}), 400
@app.route('/quiz/api/v1.0/questionnaire/question/<int:question_id>', methods=['PUT'])
def update_question( question_id):
    print(request.json)
    if not request.json:
        abort(400)
    # si la longueur de la request est inferieur ou egale 6
    elif len(request.json) <= 6:
        print(1)
        mettre_a_jour_question_simple(question_id, request.json.get('title', ''), request.json.get('choix1',''),request.json.get('choix2',''),request.json.get('reponse', ''))
        return jsonify({'result': True})
    elif len(request.json) > 6:
        print(2)
        mettre_a_jour_question_multiple(question_id, request.json.get('title', ''), request.json.get('choix1',''),request.json.get('choix2',''),request.json.get('choix3',''),request.json.get('choix4',''),request.json.get('reponse', ''))
        return jsonify({'result': True})
    return jsonify({'result': False})

@app.route('/quiz/api/v1.0/questionnaire/question/<int:question_id>', methods=['DELETE'])
def delete_question(question_id):
    """
        Delete a question
        Args:
            question_id (int): Id of the question
        Returns:
            None
    """
    print(question_id)
    supprimer_question(question_id)
    return jsonify({'result': True})