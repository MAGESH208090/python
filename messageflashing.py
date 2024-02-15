from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'any random string'

@app.route('/')
def home():
    return render_template('mflash.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    # For simplicity, we'll assume the username should be 'admin' and the password should be 'password'
    if username == 'admin' and password == 'password':
        flash('Logged in successfully!')
        return redirect(url_for('home'))
    else:
        flash('Invalid credentials. Please try again.')
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)