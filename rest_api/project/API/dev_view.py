from flask import Blueprint

devs = Blueprint('home', __name__)

@devs.route('/')
def home():
    return 'Testando'