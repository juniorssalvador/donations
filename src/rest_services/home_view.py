from flask import Blueprint, render_template
from util.api_key import require_apy_key
home_view = Blueprint('home_view', __name__)


@home_view.route('/')
@require_apy_key
def index():
    return 'Donations project'
