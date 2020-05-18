from flask import jsonify
from database.models import Category
from app import db


class CategoryController:

    def get_all(self):

        try:
            cats = Category.query.all()
            return jsonify([cat.serialize() for cat in cats])
        except Exception as e:
            return str(e)

    def add_category(self, name, description):
        cat = Category(name, description)
        db.session.add(cat)
        db.session.commit()

        return 'Ok, id={}'.format(cat.id)
