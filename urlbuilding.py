from flask import Flask,redirect,url_for
app = Flask(__name__)

@app.route('/admin')
def hello_admin():
    return 'hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return f'hello Guest {guest}'

@app.route('/user/<user>')
def hello_user(user):
    if user == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest',guest=user))
    
if __name__ == '__main__':
    app.run(debug=True)