from flask import jsonify
from database.models import States
from app import db


class StateController:

    def get_all(self):

        try:
            states = States.query.all()
            return jsonify([state.serialize() for state in states])
        except Exception as e:
            return str(e)

    def add_states(self, name):

        state = States(name)
        db.session.add(state)
        db.session.commit()

        return 'Cadastro Realizado, id={}'.format(state.id)
