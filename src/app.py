from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('config.DevelopmentConfig')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from rest_services.home_view import home_view
from rest_services.person_rest import person_rest
from rest_services.category_rest import category_rest
from rest_services.states_of_donations import state_rest

app.register_blueprint(home_view)
app.register_blueprint(person_rest)
app.register_blueprint(category_rest)
app.register_blueprint(state_rest)


@app.errorhandler(404)
def url_404(e):
    return 'not found'


app.register_error_handler(404, url_404)
