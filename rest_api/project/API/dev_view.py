from flask import Blueprint, request, jsonify
from project.utils.data import get_developer, post_developer_name
from project.utils.data import post_developer_tecnologie
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

