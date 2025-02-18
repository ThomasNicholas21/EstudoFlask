from flask import Blueprint, request, jsonify
from project.utils.data import get_developer

devs = Blueprint('home', __name__)
DEV_LIST = []

@devs.route('/', methods=['GET'])
def home():
    return DEV_LIST

@devs.route('/<string:developer>', methods=['GET', 'POST'])
def dev_name(developer):
    if request.method == 'GET':
        
        get_dev_name = get_developer(developer, DEV_LIST)

        return jsonify(get_dev_name)
    
    elif request.method == 'POST':
        DEV_LIST.append(developer) # teste
        return 'ocorrera um armazenamento aqui'
    
    return 'Método inválido'

@devs.route('/<string:developer>/<string:tecnologies>')
def dev_tecnologies(developer, tecnologies):
    return 'ocorrera alguma coisa aqui'

