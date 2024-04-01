from flask import Flask
import json
pets = json.load(open('pets.json'))
print(pets)

def create_app():
    app = Flask(__name__)
    app.config['TEMPLATES_AUTO_RELOAD'] = True

    @app.route('/')
    def hello():
        return 'Hello, PetFax!'

    from .pet import bp as pet_bp
    app.register_blueprint(pet_bp)

    from .facts import bp as facts_bp
    app.register_blueprint(facts_bp)
    
    return app