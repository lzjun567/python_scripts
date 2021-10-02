import re

from flask import Flask, jsonify, request
from webargs import fields
from webargs.flaskparser import use_args

app = Flask("hello")


@app.route("/api/login", methods=["POST"])
@use_args({"username": fields.Str(required=True)},
          location="json")
def login(args):
    name = args['username']
    password = args['password']
    return jsonify({"code": 200, "msg": "ok"})


@app.route("/api/login", methods=["POST"])
def login3():
    data = request.get_json()
    email = data.get("email")
    if not email or re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
        return jsonify({"code": 400, "msg": "参数有误"}), 400
    password = data.get("password")
    if not password or len(password) < 6:
        return jsonify({"code": 400, "msg": "参数有误"}), 400
    # 数据库查询
    return jsonify({"code": 200, "msg": "ok"})


from webargs import fields, ValidationError


def must_exist_in_db(val):
    if val != 1:
        raise ValidationError("id not exist")


hello_args = {"name": fields.Str(missing="Friend"),
              "id": fields.Integer(required=True, validate=must_exist_in_db)}


@app.route("/", methods=["GET"])
@use_args(hello_args, location="query")
def hello(args):
    """A welcome page."""
    return jsonify({"message": "Welcome, {}!".format(args["name"])})


@app.errorhandler(422)
@app.errorhandler(400)
def handle_error(err):
    headers = err.data.get("headers", None)
    messages = err.data.get("messages", ["Invalid request."])
    if headers:
        return jsonify({"errors": messages}), err.code, headers
    else:
        return jsonify({"errors": messages}), 400


#

if __name__ == '__main__':
    app.run(port=5000)
