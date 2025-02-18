from flask import Blueprint

devs = Blueprint('home', __name__)
LISTA_DEV = []

@devs.route('/', methods=['GET'])
def home():
    return LISTA_DEV

@devs.route('/<string:developer>')
def dev_name(developer):
    return 'developer'