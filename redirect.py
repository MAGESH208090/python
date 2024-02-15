from flask import Flask, request, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'any random string'  # add this line

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST' and request.form['name'] == 'admin':  # change 'username' to 'name'
        session['username'] = request.form['name']  # change 'username' to 'name'
        return redirect(url_for('success'))
    return redirect(url_for('index'))

@app.route('/success')
def success():
    return 'logged in successfully'

if __name__ == '__main__':
    app.run(debug=True)