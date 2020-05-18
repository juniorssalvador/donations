from flask import jsonify
from database.models import Person
from app import db

class PersonController:


    def get_all(self):

        try:
            persons = Person.query.all()
            return jsonify([person.serialize() for person in persons])
        except Exception as e:
            return str(e)
    
    def add_person(self,name):

        person = Person(name)
        db.session.add(person)
        db.session.commit()

        return 'Cadastro Realizado, id={}'.format(person.id)
        





