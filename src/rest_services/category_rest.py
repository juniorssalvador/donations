from flask import Blueprint
from controllers.category_controller import CategoryController

category_rest = Blueprint('category_rest', __name__)

category_con = CategoryController()


@category_rest.route('/category/all')
def index():
    return category_con.get_all()


@category_rest.route('/category/add/<category_name>/<category_desc>')
def add(category_name=None, category_desc=None):
    if category_name is None or len(category_name) == 0:
        return 'name required'
    else:
        return category_con.add_category(name=category_name, description=category_desc)
