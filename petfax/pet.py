import json
pets = json.load(open('pets.json'))
print(pets)
from flask import ( Blueprint, render_template )
bp = Blueprint('pet', __name__, url_prefix="/pets")

@bp.route('/')
def index():
    return render_template('index.html', pets=pets)


@bp.route('/<int:pet_id>')
def show(pet_id): # pet_id == 1
    for num in range(len(pets)): # for num == 0 in [0, 1, 2]:
        if pets[num]["pet_id"] == pet_id: # 1 == 1 == true
            return render_template('show.html', pet=pets[num])
    return "404 not found"

