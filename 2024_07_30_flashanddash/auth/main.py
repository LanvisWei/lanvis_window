from flask import Blueprint,render_template, request
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField
from wtforms.validators import DataRequired, Length

auth_blueprint = Blueprint('auth',__name__)

class loginForm(FlaskForm):
    email = EmailField('enter your email',validators=[DataRequired()])
    password = PasswordField('enter your passwords',validators=[DataRequired(), Length(min=4, max=20)])

@auth_blueprint.route("/auth/",methods=["get","post"])
@auth_blueprint.route("/auth/login",methods=["get","post"])
def index():
    form = loginForm()
    if request.method == "POST":
        if form.validate_on_submit():
            print("表單傳送過來")
            print("驗證了token")
            email = form.email.data
            password = form.password.data
            print(f'email:{email}')
            print(f'password:{password}') 
    else:
        print("這是第一次進入")

    return render_template('/auth/login.html.jinja', form=form)