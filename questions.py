from flask import Blueprint
# создаем объект компонента
question_bp = Blueprint('question', __name__, url_prefix="/question")

@question_bp.route("/")
def question():
    return "Hello from question"
