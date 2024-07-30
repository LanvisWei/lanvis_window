from flask import Blueprint,render_template

auth_blueprint = Blueprint('auth',__name__)

@auth_blueprint.route("/auth/",methods=["get","post"])
@auth_blueprint.route("/auth/login",methods=["get","post"])
def index():
    return render_template('/auth/login.html.jinja')