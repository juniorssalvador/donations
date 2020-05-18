from flask import Blueprint
from controllers.person_controller import PersonController
person_rest = Blueprint('person_rest',__name__)

person_con = PersonController()
@person_rest.route('/person/all')
def index():
    return person_con.get_all()
@person_rest.route('/person/add/<person_name>')
def add(person_name = None):
    if person_name == None or len(person_name) == 0:
        return 'Informe um Nome'
    else:
        return person_con.add_person(name = person_name)


