from flask import Blueprint, request, jsonify
from project.utils.data import get_developer, post_developer_name

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
        
        post_developer_name(developer, DEV_LIST)

        return 'processamento'
    
    return 'Método inválido'

@devs.route('/<string:developer>/<string:tecnologies>', methods=['GET', 'POST'])
def dev_tecnologies(developer, tecnologies):
    if request.method == 'GET':
        return 'GET'
    
    elif request.method == 'POST':
        return 'POST'
    
    return 'Método inválido'

