from flask import Flask, render_template
from flask_login import login_user
from werkzeug.utils import redirect

from data import db_session
from data.LoginForm import LoginForm
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandex_secret_key'


def main():
    app.run()


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        user = session.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


if __name__ == '__main__':
    main()
