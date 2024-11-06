from flask import Blueprint
from controllers.home_controller import HomeController

bp = Blueprint('home', __name__)

bp.route('/', methods=['GET'])(HomeController.home)
