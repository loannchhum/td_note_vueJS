from app import app
from models import get_all_questionnaires
from flask import jsonify

@app.route('/', methods=['GET'])
def all_questionnaires():
    """
        Get all questionnaires
        Args:
            None
        Returns:
            list: List of all questionnaires
    """
    return jsonify({"questionnaires": get_all_questionnaires()})
