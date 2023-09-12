from flask_app import app
from flask import redirect,request,render_template
from flask_app.model.user import User

@app.route('/')
def all_users():
    all_users = User.show_all()
    print(all_users)
    return render_template('index.html', users=all_users)

@app.route('/form')
def add_user():
    return render_template("form.html")

@app.route('/add', methods=['POST'])
def create_user():
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email']
    }
    User.add_user(data)
    return redirect('/')
    

