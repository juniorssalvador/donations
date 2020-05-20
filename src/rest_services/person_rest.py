from flask import Blueprint
from controllers.person_controller import PersonController
from util.api_key import require_apy_key

person_rest = Blueprint('person_rest', __name__)

person_con = PersonController()


@person_rest.route('/person/all')
@require_apy_key
def index():
    return person_con.get_all()


@person_rest.route('/person/add/<person_name>')
@require_apy_key
def add(person_name=None):
    if person_name is None or len(person_name) == 0:
        return 'Informe um Nome'
    else:
        return person_con.add_person(name=person_name)
