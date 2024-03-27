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


@app.route('/quiz/api/v1.0/questionnaire/', methods=['POST'])
def create_questionnaire():
    """
        Create a questionnaire
        Args:
            None
        Returns:
            json: The created questionnaire
    """
    if not request.json or not 'name' in request.json:
        abort(400)
    questionnaire = Questionnaire(name=request.json['name'])
    create_questionnaire(questionnaire)
    return jsonify({'questionnaire': questionnaire.to_json()}), 201



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
    return jsonify({'questions': [question.to_json() for question in questions]})