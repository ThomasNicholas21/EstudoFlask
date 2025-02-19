from flask import Blueprint, request, jsonify
from project.utils.data import get_developer, post_developer_name
from project.utils.data import post_developer_tecnologie
import json

devs: Blueprint = Blueprint('home', __name__)
DEV_LIST = []

@devs.route('/', methods=['GET'])
def home():
    return DEV_LIST


@devs.route('/dev/<int:id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def dev_name(id):
    developer_name = json.loads(request.data)

    if request.method == 'GET':
        
        get_dev_name = get_developer(id, DEV_LIST)

        return jsonify(get_dev_name)
    
    elif request.method == 'POST':
        
        post_developer_name(developer_name, DEV_LIST)

        return jsonify(get_dev_name)

    elif request.method == 'PUT':
        ...
    
    elif request.method == 'DELETE':
        ...
    
    return 'Invalid Method'


@devs.route('/<string:developer>/tecnologies', methods=['POST'])
def dev_tecnologies(developer):
    tecnologies = json.loads(request.data)
    
    if request.method == 'POST':

        post_developer_tecnologie(developer, tecnologies, DEV_LIST)

        return jsonify(tecnologies)
    
    return 'Invalid Method'

