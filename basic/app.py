from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Possível utilizar mais de um método
@app.route('/<int:id>', methods=['GET'])
def person(id):
    student = {
        'id': id,
        'name': 'Thomas',
        'profession': 'Software Engineer',
        'technologies': ['Python', 'Django', 'Flask', 'SQL']
    }

    return jsonify(student)

# Somente possível testar com Postman
@app.route('/sum_values', methods=["POST", "GET"])
def sum_values():
    if request.method == "POST":
        data = json.loads(request.data)
        total = sum(data['values'])

    elif request.method == "GET":
        total= 13 + 5
    
    return jsonify({'Sum: ': total})


if __name__ == "__main__":
    app.run()