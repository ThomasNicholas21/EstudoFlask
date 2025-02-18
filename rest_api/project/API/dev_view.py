from flask import Blueprint, request

devs = Blueprint('home', __name__)
LISTA_DEV = []

@devs.route('/', methods=['GET'])
def home():
    return LISTA_DEV

@devs.route('/<string:developer>', methods=['GET', 'POST'])
def dev_name(developer):
    if request.method == 'GET':
        return developer
    
    elif request.method == 'POST':
        return 'ocorrera um armazenamento aqui'
    
    return 'Método inválido'