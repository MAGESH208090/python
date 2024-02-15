from flask import Flask, request, make_response, render_template
# import the Flask class from the flask module

app = Flask(__name__)
# create an instance of the Flask class called app

@app.route('/') # the route() decorator tells Flask what URL should trigger our function
def index():
    return render_template('setcookie.html')

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['name']
        resp = make_response(render_template('readcookie.html'))
        resp.set_cookie('userID', user)
        return resp
    
@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    return '<h1>welcome ' + name + '</h1>'

if __name__ == '__main__':
    app.run(debug=True)