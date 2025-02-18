from flask import Flask

def aplicattion():

    app = Flask(__name__)

    # registra blueprints e realiza importações
    from project.API.dev_view import devs
    app.register_blueprint(devs)

    return app
