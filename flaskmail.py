from flask import Flask, request, render_template
from flask_mail import Mail, Message

app = Flask(__name__)

# Configuration for Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'magesh208090@gmail.com'
app.config['MAIL_PASSWORD'] = 'lsjg tbxe btoc fhwy'

mail = Mail(app)

@app.route('/')
def index():
    return render_template('email.html')

@app.route('/send-email', methods=['POST'])
def send_email():
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']

    msg = Message(subject, sender='magesh208090@gmail.com', recipients=[email])
    msg.body = message
    mail.send(msg)

    return 'Email has been sent!'

if __name__ == '__main__':
    app.run(debug=True)