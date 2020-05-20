from flask import Blueprint
from controllers.states_cotroller import StateController
from util.api_key import require_apy_key

state_rest = Blueprint('state_rest', __name__)
state_con = StateController()


@state_rest.route('/states/all')
@require_apy_key
def index():
    return state_con.get_all()


@state_rest.route('/states/add/<state_name>')
@require_apy_key
def add(state_name=None):
    if state_name is None or len(state_name) == 0:
        return 'Informe um Nome'
    else:
        return state_con.add_states(name=state_name)
