from flask import Blueprint
from controllers.generate_controller import GenerateController

bp = Blueprint('generate', __name__, url_prefix='/api/generate')


bp.route('/pdf', methods=['POST'])(GenerateController.generate)

