from flask import Blueprint
from flask.json import jsonify
from models import User

bp = Blueprint("user", __name__)


# 查询所有用户
@bp.route("/query_all", methods=['GET', 'POST'])
def query_all():
    users = User.query.all()
    result = list(map(User.to_json, users))
    return jsonify(result)
