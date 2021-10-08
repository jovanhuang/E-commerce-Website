from market import app
from flask import render_template, redirect, url_for
from market.models import Item, User
from market.forms import RegisterForm
from market import db

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')


@app.route("/market")
def market_page():
    items = Item.query.all()
    return render_template("market.html", items = items)

@app.route("/register", methods = ['GET', 'POST'])
def register_page():
    form = RegisterForm()
    # Will come here if meet all validators in forms.py.
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data, 
                              email_address=form.email_address.data,
                              password_hash=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    # in-built dict that will contain all the errors in the forms.py if any.
    if form.errors != {}: #If there are no errors from validations of forms.py for registration
        for err_msg in form.errors.values():
            print(f'There was an error with creating an account: {err_msg}')
    return render_template("register.html", form=form)