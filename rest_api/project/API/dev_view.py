from flask import Blueprint, request, jsonify
from project.utils.data import get_developer, post_developer_name
from project.utils.data import update_developer_name, delete_developer
import json


devs: Blueprint = Blueprint('home', __name__)
DEV_LIST = []


@devs.route('/', methods=['GET'])
def home():
    return DEV_LIST


@devs.route('/dev/<int:id>', methods=['GET'])
def get_dev_name(id):
    if request.method == 'GET':
        get_dev_name = get_developer(id, DEV_LIST)

        return jsonify(get_dev_name)

    return 'Invalid Method'


@devs.route('/dev/post', methods=['POST'])
def post_dev_name():
    developer = json.loads(request.data)

    if request.method == 'POST':
        post_developer_name(developer, DEV_LIST)

        return 'Developer Created'
    
    return 'Invalid Method'


@devs.route('/dev/<int:id>/update', methods=['PUT'])
def update_dev_name(id):
    developer = json.loads(request.data)

    if request.method == 'PUT':
        update_developer_name(developer, id, DEV_LIST)

        return 'User updated'
    
    return 'Invalid Method'


@devs.route('/dev/<int:id>/delete', methods=['DELETE'])
def delete_dev_name(id):
    if request.method == 'DELETE':
        delete_developer(id, DEV_LIST)

        return 'Developer Deleted'
    
    return 'Invalid Method'
