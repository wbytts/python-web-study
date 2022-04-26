from flask import Blueprint
from werkzeug.routing import BaseConverter

bp = Blueprint("test", __name__)


@bp.route('/', methods=['GET'])
def test():
    return '这里是test！'


@bp.route('/user/<name>')
def router_001(name):
    return 'success'


@bp.route('/jinja2/001')
def jinja2_001():
    pass
